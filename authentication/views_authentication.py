from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .models import Coordinator, Volunteer, Secretary
from validate_email import validate_email
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from .models import stats
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.urls import reverse
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .commonPasswords import common_passwords
from .captcha import FormWithCaptcha


def LoginView(request):
    if request.method == 'GET':
        messages.success(request, 'Welcome to our new website! Your password would be your email that you entered during registration.')
        messages.info(request, 'If you aren\'t able to login then please contact your coordinator.')
        return render(request, 'login.html', {"form":FormWithCaptcha()})
    else:
        if not FormWithCaptcha(request.POST).is_valid():
            messages.error(request, 'Please verify that you are not a robot.')
            return redirect('login')
        email = request.POST['email']
        email = email.strip()
        email = email.lower()
        password = request.POST['password']
        password = password.strip()
        if '@vit.edu' not in email:
            messages.error(request, 'Please login with your college email ID ending with @vit.edu')
            return redirect('login')
        if not validate_email(email):
            messages.error(request, '"' + email + '" is an invalid email address. Please enter your correct mail address.')
            return redirect('login')
        try:
            username = User.objects.get(email=email).username
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'We found no account associated with ' + email)
            messages.info(request, 'Simple Solution: You might have entered incorrect email. Please enter your college email which you had entered at the time of registration!')
            return redirect ('login')


        if user.first_name == 'Coordinator':
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                s = stats.objects.get(index=1)
                s.totalLogins += 1
                s.save()
                messages.success(request, 'Hurray! You\'re now logged in!')
                return redirect('CDashboard')
            else:
                messages.error(request, 'Wrong credentials.')
                return redirect('login')
        elif user.first_name == 'Secretary':
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                s = stats.objects.get(index=1)
                s.totalLogins += 1
                s.save()
                messages.success(request, 'Hurray! You\'re now logged in!')
                return redirect('SDashboard')
            else:
                messages.error(request, 'Wrong Credentials.')
                return redirect('login')
        elif user.first_name == 'Volunteer':
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                s = stats.objects.get(index=1)
                s.totalLogins += 1
                s.save()
                messages.success(request, 'Hurray! You\'re now logged in!')
                return redirect('vdashboard')
            else:
                messages.error(request, 'Wrong credentials.')
                return redirect('login')
        else:
            messages.error(request, 'Oops! There was a problem in logging you in. Please mail to vitswd@vit.edu')
            return redirect('login')

def LoginRestrictedView(request):
    messages.error(request, "Your session has expired. Please login again.")
    return render(request, 'login_restricted.html', {"form":FormWithCaptcha()})

def LogoutView(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'You have been logged out successfully!')
        return redirect('login')
    else:
        messages.error(request, 'Your session has expired. Please login again.')
        return redirect('login')



def RequestPasswordResetEmail(request):
    if request.method == "GET":
        return render(request, 'resetpassword.html', {"form":FormWithCaptcha()})
    else:
        if not FormWithCaptcha(request.POST).is_valid():
            messages.error(request, 'Please verify that you are not a robot.')
            return redirect('reset')
        email = request.POST['email']
        email = email.strip()
        email = email.lower()
        if not User.objects.filter(email=email).exists() or not validate_email(email):
            messages.error(request, 'The email ' + email + ' is not registered with us!')
            messages.info(request, 'Re-check the email and enter the correct one!')
            return redirect('reset')
        user = User.objects.get(email=email)
        if user.first_name == 'Volunteer':
            user_object = Volunteer.objects.get(email=email)
            if user_object.password_changed == False:
                messages.error(request,   'There is no need to receive a reset link to reset your password as your password is your email. You have not changed it after logging in. So, use your email as your password to login.')
                return redirect ('login')
        elif user.first_name == "Coordinator":
            user_object = Coordinator.objects.get(email=email)
        elif user.first_name == 'Secretary':
            user_object = Secretary.objects.get(email=email)
        if user_object.password_changed == False:
            messages.error(request,   'There is no need to receive a reset link to reset your password as your password is your email. You have not changed it after logging in. So, use your email as your password to login.')
            return redirect ('login')
        current_site = get_current_site(request)

        email_contents = {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user)),
                    'token': PasswordResetTokenGenerator().make_token(user)}
        link = reverse('setnewpassword', kwargs={'uidb64': email_contents['uid'], 'token': email_contents['token']})
        email_subject = 'Reset password for your SWDC Account'
        reset_url = 'https://'+current_site.domain+link
        email = EmailMessage(
                    email_subject,
                    'Hi '+user.username+', \n\nPlease click the link below to set a new password for your account.\n\n' + reset_url + '\n\nRegards,\nThe Social Welfare Development Committee',
                    'noreply@semycolon.com',
                    [email])
        email.send(fail_silently=False)
        messages.success(request, 'We\'ve sent a mail with the link to ' + str(request.POST['email']))
        return redirect('reset')


def SetNewPasswordView(request,uidb64, token):
    context = {'uidb64': uidb64, 'token': token, 'form': FormWithCaptcha()}
    if request.method=="GET":
        try:
            username_decoded = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(username=username_decoded)
            if not PasswordResetTokenGenerator().check_token(user, token):
                messages.info(request, 'Password link is invalid or has been used earlier, please request a new one.')
                return redirect('reset')
        except Exception as a:
            messages.error(request, 'Something went wrong, request a new link again.')
            return redirect('reset')
        messages.success(request, "Please set a new password for your account.")
        return render(request, 'setnewpass.html', context)
    else:
        if not FormWithCaptcha(request.POST).is_valid():
            messages.error(request, 'Please verify that you are not a robot.')
            return render(request, 'setnewpass.html', context)
        context = {'uidb64':uidb64,'token':token}
        password = request.POST['password']
        password2 = request.POST['password2']
        password = password.strip()
        password2 = password2.strip()
        if password != password2:
            messages.error(request, 'Passwords do not match. Re-enter both again.')
            return render( request, 'setnewpass.html', context)
        if len(password) < 6:
            messages.error(request, 'Enter a password greater than 6 characters.')
            return render( request, 'setnewpass.html', context)
        if password in common_passwords:
            messages.error(request, 'This password is too common.')
            return render( request, 'setnewpass.html', context)
        try:
            username_decoded = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(username=username_decoded)
            user.set_password(password)
            user.save()
            if user.first_name == 'Volunteer':
                volunteer = Volunteer.objects.get(email=user.email)
                volunteer.password_changed = True
                volunteer.save()
            elif user.first_name == 'Coordinator':
                coord = Coordinator.objects.get(email=user.email)
                coord.password_changed = True
                coord.save()
            elif user.first_name == 'Secretary':
                sec = Secretary.objects.get(email=user.email)
                sec.password_changed = True
                sec.save()
            messages.success(request, 'Your password has been changed successfully. You can login with the new password.')
            return redirect('login')
        except Exception as ex:
            messages.info(request, 'Something went wrong, please request a new link.')
            return redirect('reset')