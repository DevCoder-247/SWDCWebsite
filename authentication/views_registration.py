from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Coordinator, Volunteer, Secretary, Activity, currentData, Departments, Domain, stats, DomainAllotment
from .captcha import FormWithCaptcha
from validate_email import validate_email
from django.conf import settings
import os 

def Format_Name_Function(name):
    formatted_name = name[0].upper()
    i = 1
    while i < len(name):
        if name[i] == ' ':
            if name[i + 1] == ' ':
                i += 1
                continue
            formatted_name += ' ' + name[i + 1].upper()
            i += 1
        else:
            formatted_name += name[i].lower()
        i += 1
    return formatted_name

def checkName(name):
    for c in name:
        if not c.isalpha() and c != ' ':
            return False
    return True

def VolunteerRegistrationView(request):
    if request.method == 'GET':
        activities = Activity.objects.filter(registration_enabled=True)
        t_and_c = {}
        for activity in activities:
            t_and_c[activity.name] = activity.t_and_c
        departments = Departments.objects.all()
        return render(request, 'vregistration.html', {'activities' : activities, 't_and_c': t_and_c, 'departments': departments, "form":FormWithCaptcha()})

    if request.method == 'POST':
        if not FormWithCaptcha(request.POST).is_valid():
            messages.error(request, 'Please verify that you are not a robot.')
            return redirect('vreg')

        name = request.POST['name']
        name = Format_Name_Function(name.strip())

        emailVal = request.POST['email']
        emailVal = emailVal.strip()
        emailVal = emailVal.lower()
        emailAgain = request.POST['emailAgain']
        emailAgain = emailAgain.strip()
        emailAgain = emailAgain.lower()

        gender = request.POST['gender']
        user_entered_activity = request.POST['activity']
        dept = request.POST['dept']
        academic_year = request.POST['academic_year']
        div = request.POST['div']
        current_add = request.POST['current_add']
        current_add = current_add.strip()
        prn = request.POST['prn']
        prn = prn.strip()
        prnAgain = request.POST['prnAgain']
        prnAgain = prnAgain.strip()
        roll = request.POST['roll']
        roll = roll.strip()
        contact_num = request.POST['number']
        contact_num = contact_num.strip()
        parent_num = request.POST['parent_num']
        parent_num = parent_num.strip()
        blood_group = request.POST['blood_group']
        blood_group = blood_group.strip()

        # print('Initial div: ', div)

        activity = Activity.objects.get(name=user_entered_activity)
        check = currentData.objects.get(index='Current').AcademicYear[2:4]

        if emailAgain != emailVal:
            messages.error(request, 'You were asked to enter your email twice for a cross check. You had entered it as ' + emailVal + ' and ' + emailAgain)
            messages.info(request, 'These two do not match, so please enter your correct mail ID twice and click on the register button.')
            return redirect('vreg')

        if prn != prnAgain:
            messages.error(request, 'You were asked to enter your PRN twice for a cross check. You had entered it as ' + prn + ' and ' + prnAgain)
            messages.info(request, 'These two do not match, so please enter your correct PRN twice and click on the register button.')
            return redirect('vreg')


        if check not in emailVal:
            messages.error(request, emailVal + ' does not seem to be an email ID of a FY student. Only students of first year are allowed to register.')
            return redirect('vreg')

        if '@vit.edu' not in emailVal or not validate_email(emailVal):
            messages.error(request, emailVal + ' is an incorrect mail ID. Enter your correct college mail ID ending with @vit.edu')
            return redirect('vreg')

        if not checkName(name):
            messages.error(request, 'You entered your name as ' + name +'. But it cannot contain special characters or numbers.')
            return redirect('vreg')

        if gender == 'Male' and activity.only_females==True:
            messages.error(request, user_entered_activity + ' is only for females. Please register for any of the other available activities.')
            return redirect('vreg')

        if gender == 'Female' and activity.only_males==True:
            messages.error(request, user_entered_activity + ' is only for males. Please register for any of the other available activities.')
            return redirect('vreg')

        if activity.current_count >= activity.max_count:
            # activity.registration_enabled = False
            # activity.save()
            messages.error(request, 'Hey! We regret to inform you that the registrations are closed for ' + user_entered_activity + ' because slots are full.')
            messages.info(request, 'There are a fixed number of registrations that we accept for each activity, and once slots are full, registrations are closed even though there is still time for the registration deadline.')
            return redirect('vreg')

        # Allow failed volunteers:
        earlierFailed = ''
        if activity.allow_failed_volunteers:
            if Volunteer.objects.filter(email = emailVal).exists():
                v = Volunteer.objects.get(email = emailVal)
                if v.verified == 3:
                    earlierFailed = v.activity
                    user = User.objects.get(email = emailVal)
                    user.delete()
                    v.delete()
                    s = stats.objects.get(index=1)
                    s.vCount -= 1
                    s.uCount -= 1
                    s.save()



        if Volunteer.objects.filter(email = emailVal).exists():
            v = Volunteer.objects.get(email = emailVal)
            current = currentData.objects.get(index='Current')

            if v.registered_academic_year == current.AcademicYear and v.registered_semester == current.Semester:
                if v.verified == 3:
                    messages.error(request, 'You have already been failed in ' + v.activity + ' so you cannot register in another activity again.')
                else:
                    volunteerActivityObj = Activity.objects.get(name = v.activity)
                    if not volunteerActivityObj.registration_enabled:
                        messages.error(request, 'Hello ' + v.vname + ', you had previously registered for ' + v.activity + ' in this semester. So you cannot register for another activity in this semester.')
                        messages.info(request, 'Please note that this is not an "ERROR" in the website. This is a rule of the SWD Committee that one cannot particiapte in two activities in the same semester even if one was/wasn\'t able to clear the previous activity (' +  v.activity + ' in your case)')
                    else:
                        messages.success(request, 'Hello ' + v.vname + ', we have already received your registration for ' + v.activity + ' for this semester. We will soon reach out to you!')
            else:
                if v.verified == 1:
                    messages.success(request, 'Hi ' + v.vname + ', you have already cleared your Social Services Course by participating in ' + v.activity + ' during Academic Year ' + v.registered_academic_year + ' Semester ' + str(v.registered_semester) + '. So you will not be able to participate in ' + user_entered_activity)
                    messages.success(request, 'But be assured that you have passed in the Social Services Course and it will reflect in your marksheet received at the end of your first year')
                elif v.verified == 3:
                    messages.info(request, 'Hi ' + v.vname + ', you had registered earlier for ' + v.activity + ' during Academic Year ' + v.registered_academic_year + ' Semester ' + str(v.registered_semester) + ', but you have been failed in the Social Services Course.')
                    messages.error(request, 'You cannot register for ' + user_entered_activity)
                    messages.info(request, 'But there are some activities which allow failed volunteers, so please choose any other activity and try registering.')
            return redirect('vreg')

        if Volunteer.objects.filter(vname = name).exists():
            messages.error(request, 'A user with the name ' + name + ' has already registered on the website. So please enter your full name or your name with your initial so that we can distinguish both of you.')
            return redirect('vreg')

        if Volunteer.objects.filter(email = emailVal).exists():
            messages.error(request, 'A user with mail ID ' + emailVal + ' has registered on the website. Please mail to us at vitswd@vit.edu')
            return redirect('vreg')

        if Volunteer.objects.filter(prn = prn).exists():
            messages.error(request, 'Seems like someone else has registered with your PRN number. Please mail to us at vitswd@vit.edu!')
            return redirect('vreg')

        if Volunteer.objects.filter(contact_num = contact_num).exists():
            messages.error(request, 'Seems like someone else has registered with your mobile number. Please mail to us at vitswd@vit.edu!')
            return redirect('vreg')

        if User.objects.filter(username = name).exists():
            messages.error(request, 'A user with the name ' + name + ' has already registered on the website. So please enter your full name or your name with your initial so that we can distinguish both of you.')
            return redirect('vreg')

        if User.objects.filter(email = emailVal).exists():
            messages.error(request, 'A user with mail ID ' + emailVal + ' has registered on the website. Please mail to us at vitswd@vit.edu')
            return redirect('vreg')
        
        vol_dept_div = dept + '-' + div
        vol_domain = ''

        domains = DomainAllotment.objects.all()
        divisions_having_domain = []

        for domain in domains:
            divisions = domain.divisions.split(',')
            if vol_dept_div in divisions:
                vol_domain = domain.name
            for divi in divisions:
                divisions_having_domain.append(divi)
        
        

        if vol_dept_div not in divisions_having_domain:
            messages.error(request, 'Your division hasn\'t been allotted a domain yet.')
            return redirect('vreg')

        user = User.objects.create_user(username=name, email=emailVal, first_name="Volunteer")
        user.is_active = True
        user.set_password(str(prn))
        user.save()



        currentInfo = currentData.objects.get(index='Current')
        # print('div ', div)
        reg = Volunteer.objects.create(vname=name, email=emailVal, gender=gender, activity=user_entered_activity, dept=dept,academic_year=academic_year, registered_academic_year = currentInfo.AcademicYear, registered_semester = currentInfo.Semester, div=div, current_add=current_add, prn=prn, roll=roll, contact_num=contact_num, Cordinator='', parent_num=parent_num, blood_group=blood_group, domain=vol_domain)
        reg.save()

        s = stats.objects.get(index=1)
        s.vCount += 1
        s.uCount += 1
        s.save()
        activity.current_count += 1
        activity.save()
        if earlierFailed != '':
            messages.info(request, 'Hi ' + name + ', you had earlier registered for ' + earlierFailed + ' but you had been failed in ' + earlierFailed + '. The SWD Committee is giving you a second and last chance to clear the Social Services Course by allowing you to participate in ' + user_entered_activity)
            messages.error(request, 'Note that you have to compulsorily clear ' + user_entered_activity + ' in this semester or else you will be permanently failed.')
            messages.success(request, 'We will soon reach out to you for participating in ' + user_entered_activity)
        else:
            messages.success(request, 'Hurray!! Your registration is successfull.')
            messages.success(request, 'We will soon reach out to you for participating in ' + user_entered_activity)
        return render(request, 'registration_successful.html')


def CoordRegistrationView(request):
    if request.method == "GET":
        departments = Departments.objects.filter(enabled=True)
        activities = Activity.objects.filter(registration_enabled=True)
        domains = Domain.objects.filter(enabled=True)
        return render(request, 'creg.html', {'departments':departments, 'activities':activities, 'domains': domains, "form":FormWithCaptcha()})
    else:
        if not FormWithCaptcha(request.POST).is_valid():
            messages.error(request, 'Please verify that you are not a robot.')
            return redirect('creg')
        name = request.POST['Name']
        name = Format_Name_Function(name.strip())
        email = request.POST['email']
        email = email.strip()
        email = email.lower()
        gender = request.POST['gender']
        dept = request.POST['dept']
        academic_year = request.POST['year']
        div = request.POST['div']
        current_add = request.POST['add']
        current_add = current_add.strip()
        prn = request.POST['prn']
        prn = prn.strip()
        roll = request.POST['roll']
        roll = roll.strip()
        contact_num = request.POST['number']
        contact_num = contact_num.strip()
        user_entered_activity = request.POST['activity']
        domain = request.POST['domain']
        parent_num = request.POST['parent_num']
        parent_num = parent_num.strip()
        blood_group = request.POST['blood_group']
        blood_group = blood_group.strip()
        secret_code = request.POST['secret_code']
        secret_code = secret_code.strip()

        if secret_code != str(os.getenv('COORD_REG_PWD')):
            messages.error(request, 'Incorrect secret code!')
            return redirect('creg')

        if not checkName(name):
            messages.error(request, 'You entered your name as ' + name +'. But it cannot contain special characters or numbers.')
            return redirect('creg')

        check = currentData.objects.get(index='Current').AcademicYear[2:4]
        if check in email:
            messages.error(request, 'A student of first year cannot be a coordinator!')
            return redirect('creg')

        if '@vit.edu' not in email:
            messages.error(request, 'Your email must contain @vit.edu in it.')
            return redirect('creg')

        if User.objects.filter(email = email).exists():
            if len(Coordinator.objects.filter(email = email)) != 0:
                coordinator = Coordinator.objects.get(email = email)
                current = currentData.objects.get(index = 'Current')
                if coordinator.registered_semester == current.Semester and coordinator.registered_academic_year == current.AcademicYear:
                    messages.error(request, 'You have already registered in this semester. So you cannot register again.')
                    return redirect('creg')
                user = User.objects.get(email = email)
                user.delete()
                coordinator.delete()
            else:
                user = User.objects.get(email = email)
                user.delete()

        if Coordinator.objects.filter(prn = prn).exists():
            messages.error(request, 'Seems like someone else has registered with your PRN number. Please contact the website team!')
            return redirect('creg')

        if Coordinator.objects.filter(contact_num = contact_num).exists():
            messages.error(request, 'Seems like someone else has registered with your mobile number. Please contact the website team!')
            return redirect('creg')

        if User.objects.filter(username = name).exists():
            messages.error(request, 'A user with the name ' + name + ' has already registered on the website. So please enter your full name or your name with your initial so that we can distinguish both of you.')
            return redirect('creg')

        if User.objects.filter(email = email).exists():
            messages.error(request, 'Another user with mail ID ' + email + ' has registered on the website. Please mail to us at vitswd@vit.edu')
            return redirect('creg')


        user = User.objects.create_user(username=name, email=email, first_name='Coordinator')
        user.set_password(str(prn))
        user.is_active = True
        user.save()

        currentInfo = currentData.objects.get(index='Current')
        activityObj = Activity.objects.get(name=user_entered_activity)
        if activityObj.flagship_event == False:
            reg = Coordinator.objects.create(cname=name, email=email, gender=gender, dept=dept, academic_year=academic_year, registered_academic_year = currentInfo.AcademicYear, registered_semester = currentInfo.Semester, div=div, current_add=current_add, prn=prn, roll=roll, contact_num=contact_num, activity=user_entered_activity, domain=domain, flagshipEvent = 'not_chosen', verified=0, submitted=0, parent_num=parent_num, blood_group=blood_group)
        else:
            reg = Coordinator.objects.create(cname=name, email=email, gender=gender, dept=dept, academic_year=academic_year, registered_academic_year = currentInfo.AcademicYear, registered_semester = currentInfo.Semester, div=div, current_add=current_add, prn=prn, roll=roll, contact_num=contact_num, flagshipEvent=user_entered_activity, domain=domain, activity = 'not_chosen', verified=0, submitted=0, parent_num=parent_num, blood_group=blood_group)
        reg.save()


        s = stats.objects.get(index=1)
        s.cCount +=1
        s.uCount +=1
        s.save()
        messages.success(request, 'Hurray! Your registration for ' + user_entered_activity + ' was successful. Your Activity Head will inform you about the further process when your activity starts!')
        return render(request, 'registration_successful.html')



def SecretaryRegistrationView(request):
    if request.method == "GET":
        departments = Departments.objects.filter(enabled=True)
        domains = Domain.objects.filter(enabled=True)
        activities = Activity.objects.filter(registration_enabled=True)
        return render(request, 'sreg.html', {'departments': departments, 'domains':domains, 'activities': activities, "form":FormWithCaptcha()})
    else:
        if not FormWithCaptcha(request.POST).is_valid():
            messages.error(request, 'Please verify that you are not a robot.')
            return redirect('sreg')
        name = request.POST['Name']
        name = Format_Name_Function(name.strip())
        email = request.POST['email']
        email = email.strip()
        email = email.lower()
        gender = request.POST['gender']
        dept = request.POST['dept']
        academic_year = request.POST['year']
        div = request.POST['div']
        current_add = request.POST['add']
        current_add = current_add.strip()
        prn = request.POST['prn']
        prn = prn.strip()
        roll = request.POST['roll']
        roll = roll.strip()
        contact_num = request.POST['number']
        contact_num = contact_num.strip()
        domain = request.POST['domain']
        activity = request.POST['activity']
        secret_code = request.POST['secret_code']
        secret_code = secret_code.strip()
        if activity == 'NA':
            activity = ''
        if secret_code != str(os.getenv('SEC_REG_PWD')):
            messages.error(request, 'Incorrect secret code!')
            return redirect('sreg')

        if not checkName(name):
            messages.error(request, 'Name cannot contain special characters.')
            return redirect('sreg')

        check = currentData.objects.get(index='Current').AcademicYear[2:4]
        if check in email:
            messages.error(request, 'A student of first year cannot be a coordinator!')
            return redirect('creg')

        if '@vit.edu' not in email:
            messages.error(request, 'Your email must contain @vit.edu in it.')
            return redirect('sreg')

        if User.objects.filter(email = email).exists():
            if len(Secretary.objects.filter(email = email)) != 0:
                secretary = Secretary.objects.get(email = email)
                current = currentData.objects.get(index = 'Current')
                if secretary.registered_semester == current.Semester and secretary.registered_academic_year == current.AcademicYear:
                    messages.error(request, 'You have already registered for ' + secretary.activity + ' . So you cannot register for ' + activity)
                    return redirect('sreg')
                user = User.objects.get(email = email)
                user.delete()
                secretary.delete()
            else:
                user = User.objects.get(email = email)
                user.delete()


        if Secretary.objects.filter(prn = prn).exists():
            messages.error(request, 'Seems like someone else has registered with your PRN number. Please contact the website team!')
            return redirect('sreg')

        if Secretary.objects.filter(contact_num = contact_num).exists():
            messages.error(request, 'Seems like someone else has registered with your mobile number. Please contact the website team!')
            return redirect('sreg')

        if User.objects.filter(username = name).exists():
            messages.error(request, 'A user with the name ' + name + ' has already registered on the website. So please enter your full name or your name with your initial so that we can distinguish both of you.')
            return redirect('sreg')

        if User.objects.filter(email = email).exists():
            messages.error(request, 'A user with mail ID ' + email + ' has registered on the website. Please mail to us at vitswd@vit.edu')
            return redirect('sreg')


        user = User.objects.create_user(username=name, email=email, first_name='Secretary')
        user.set_password(str(prn))
        user.is_active = True
        user.save()

        currentInfo = currentData.objects.get(index='Current')
        reg = Secretary.objects.create(sname=name, email=email, gender=gender,  dept=dept, academic_year=academic_year, registered_academic_year = currentInfo.AcademicYear, registered_semester = currentInfo.Semester, div=div, current_add=current_add, prn=prn, roll=roll, contact_num=contact_num, domain=domain, activity=activity)
        reg.save()


        s = stats.objects.get(index=1)
        s.sCount += 1
        s.uCount += 1
        s.save()

        messages.success(request, 'Hurray your registration is complete! You may login now!')
        messages.success(request, 'Your password is your PRN.')
        return redirect('login')


def SecretaryRegistrationComplete(name, email, gender, dept, academic_year, div, current_add, prn, roll, contact_num, domain, activity):
    try:
        currentInfo = currentData.objects.get(index='Current')
        reg = Secretary.objects.create(sname=name, email=email, gender=gender,  dept=dept, academic_year=academic_year, registered_academic_year = currentInfo.AcademicYear, registered_semester = currentInfo.Semester, div=div, current_add=current_add, prn=prn, roll=roll, contact_num=contact_num, domain=domain, activity=activity)
        reg.save()
        testGet = Secretary.objects.get(email=email)
        return True
    except Exception as errorMessage:
        return False