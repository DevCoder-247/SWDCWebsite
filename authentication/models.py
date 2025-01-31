from django.db import models
import os

def profile_picture_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    new_filename = f"{instance.user.first_name}_{instance.user.username}_{instance.prn}.{ext}"
    return os.path.join('profile_pictures', new_filename)

class Volunteer(models.Model):
    vname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=30, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    domain = models.CharField(max_length=70, blank=True)
    activity = models.CharField(max_length=30, blank=True)
    dept = models.CharField(max_length=60, blank=True)
    academic_year = models.CharField(max_length=10, default='FY', blank=True)
    registered_academic_year = models.CharField(max_length=30, blank=True)
    registered_semester = models.IntegerField(blank=True)
    div = models.CharField(max_length=10, blank=True)
    current_add = models.CharField(max_length=200, blank=True)
    prn = models.BigIntegerField(blank=True)
    roll = models.BigIntegerField(blank=True)
    contact_num = models.CharField(max_length=12, blank=True)
    parent_num = models.CharField(max_length=12, blank=True)
    blood_group = models.CharField(max_length=10, blank=True)
    verified = models.IntegerField(default=0, blank=True)
    submitted = models.IntegerField(default=0, blank=True)
    ans1 = models.CharField(max_length=1500, blank=True)
    ans2 = models.CharField(max_length=1500, blank=True)
    ans3 = models.CharField(max_length=1500, blank=True)
    ans4 = models.CharField(max_length=1500, blank=True)
    ans5 = models.CharField(max_length=1500, blank=True)
    ans6 = models.CharField(max_length=1500, blank=True)
    url = models.URLField(max_length=150, blank=True)
    Cordinator = models.CharField(max_length=40, blank=True)
    guardian_faculty = models.CharField(max_length=50, default='not_assigned', blank=True)
    rejection_reason = models.CharField(max_length=200, default='none', blank=True)
    password_changed = models.BooleanField(default=False, blank=True)
    attendance = models.CharField(max_length=350, default='', blank=True)
    marked_IN_attendance = models.BooleanField(default=False)
    profile_edited = models.CharField(max_length=10, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', default='default-profile.jpg', blank=True)
    def _str_(self):
        return self.vname
    class Meta:
        ordering = ['vname']

class Coordinator(models.Model):
    cname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=30, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    dept = models.CharField(max_length=60, blank=True)
    academic_year = models.CharField(max_length=10, blank=True)
    registered_academic_year = models.CharField(max_length=30, blank=True)
    registered_semester = models.IntegerField(blank=True)
    div = models.CharField(max_length=10, blank=True)
    current_add = models.CharField(max_length=100, blank=True)
    prn = models.BigIntegerField(blank=True)
    roll = models.BigIntegerField(blank=True)
    contact_num = models.CharField(max_length=10, blank=True)
    parent_num = models.CharField(max_length=10, blank=True)
    blood_group = models.CharField(max_length=10, blank=True)
    verified = models.IntegerField(default=0)
    submitted = models.IntegerField(default=0)
    ans1 = models.CharField(max_length=1500, blank=True)
    ans2 = models.CharField(max_length=1500, blank=True)
    ans3 = models.CharField(max_length=1500, blank=True)
    ans4 = models.CharField(max_length=1500, blank=True)
    ans5 = models.CharField(max_length=1500, blank=True)
    ans6 = models.CharField(max_length=1500, blank=True)
    url = models.URLField(max_length=150, blank=True)
    Secretary = models.CharField(max_length=40, blank=True)
    activity = models.CharField(max_length=30, blank=True)
    flagshipEvent = models.CharField(max_length=30, blank=True)
    domain = models.CharField(max_length=50, blank=True)
    password_changed = models.BooleanField(default=False)
    marked_attendance_GP2 = models.BooleanField(default=False)
    marked_attendance_FE = models.BooleanField(default=False)
    marked_IN_GP2 = models.BooleanField(default=False)
    marked_IN_FE = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', default='default-profile.jpg')
    qr_codeSS = models.ImageField(upload_to='qr_codes/Social_Services/', blank=True)
    qr_codeFE = models.ImageField(upload_to='qr_codes/Flagship/', blank=True)
    def __str__(self):
        return self.cname
    class Meta:
        verbose_name_plural = 'Coordinators'
        ordering = ['cname']

class Secretary(models.Model):
    sname = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=30, blank=True)
    gender = models.CharField(max_length=10, blank=True)
    dept = models.CharField(max_length=60, blank=True)
    academic_year = models.CharField(max_length=10, blank=True)
    registered_academic_year = models.CharField(max_length=30, blank=True)
    registered_semester = models.IntegerField(default=2, blank=True)
    domain = models.CharField(max_length=50, blank=True)
    activity = models.CharField(max_length=30, blank=True)
    flagshipEvent = models.CharField(max_length=30, blank=True)
    div = models.CharField(max_length=10, blank=True)
    current_add = models.CharField(max_length=100, blank=True)
    prn = models.BigIntegerField(blank=True)
    roll = models.BigIntegerField(blank=True)
    contact_num = models.CharField(max_length=10, blank=True)
    password_changed = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to=profile_picture_upload_path, default='default-profile.jpg', blank=True)
    def __str__(self):
        return self.sname
    class Meta:
        verbose_name_plural = 'Secretaries'
        ordering = ['sname']

class stats(models.Model):
    index = models.IntegerField()
    uCount = models.IntegerField()
    vCount = models.IntegerField()
    cCount = models.IntegerField()
    sCount = models.IntegerField()
    totalLogins = models.IntegerField()
    hits = models.IntegerField()
    lastUpdated = models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural = 'Stats'

class Activity(models.Model):
    name = models.CharField(max_length=30, blank=True)
    divisions = models.CharField(max_length=50, default='', blank=True, null=True)
    registration_enabled = models.BooleanField()
    current_count = models.IntegerField(blank=True)
    max_count = models.IntegerField(blank=True)
    flagship_event = models.BooleanField()
    allow_failed_volunteers = models.BooleanField()
    only_males = models.BooleanField()
    only_females = models.BooleanField()
    report_filling = models.BooleanField()
    report_verification = models.BooleanField()
    attendance = models.BooleanField()
    t_and_c = models.CharField(max_length=1500, blank=True)
    message = models.CharField(max_length=1500, blank=True)

    # Questions for report-filling. Each activity can have it's own questions
    q1 = models.CharField(max_length=200, blank=True)
    q2 = models.CharField(max_length=200, blank=True)
    q3 = models.CharField(max_length=200, blank=True)
    q4 = models.CharField(max_length=200, blank=True)
    q5 = models.CharField(max_length=200, blank=True)
    q6 = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Activities'
        ordering = ['name']


class Event(models.Model):
    activity = models.CharField(max_length=30, blank=True)
    roll_nos = models.CharField(max_length=60, default='',null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)
    map_link = models.URLField(max_length=400, null=True, blank=True)
    description = models.TextField(blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    isOnline = models.BooleanField(default=False, blank=True)
    venue = models.CharField(max_length=100, blank=True)
    divisions = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.activity
    class Meta:
        verbose_name_plural = 'Events'
        ordering = ['-date', 'start_time']


class Attendance(models.Model):
    coord_name = models.CharField(max_length=100, null=True, blank=True)
    coord_prn = models.CharField(max_length=20, null=True, blank=True)
    vol_name = models.CharField(max_length=100, null=True, blank=True)
    vol_prn = models.CharField(max_length=20, null=True, blank=True)
    geo_photo = models.TextField(blank=True, null=True)
    actual_latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    actual_longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    time = models.DateTimeField(auto_now_add=True)
    activity = models.CharField(max_length=50, null=True)
    venue = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return self.vol_name
    class Meta:
        verbose_name_plural = 'Attendance Records'
        ordering = ['-time']


class Domain(models.Model):
    name = models.CharField(max_length=40)
    enabled = models.BooleanField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Domains'
        ordering =  ['name']

class DomainAllotment(models.Model):
    name = models.CharField(max_length=100, default='', blank=True, null=True)
    divisions = models.CharField(max_length=150, default='', blank=True, null=True)
    activities = models.CharField(max_length=150, default='', blank=True, null=True)

class currentData (models.Model):
    index = models.CharField(max_length=15)
    AcademicYear = models.CharField(max_length=20)
    Semester = models.IntegerField()
    class Meta:
        verbose_name_plural = 'Current-Data'
        ordering = ['index']

class Departments(models.Model):
    name = models.CharField(max_length=70, blank=True)
    key = models.CharField(max_length=20, blank=True)
    enabled = models.BooleanField()
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Departments'

class GuardianFaculty(models.Model):
    name = models.CharField(max_length=50)
    active = models.BooleanField()
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = 'Guardian Faculties'
        ordering = ['name']