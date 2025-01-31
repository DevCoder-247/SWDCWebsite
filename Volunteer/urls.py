from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt
urlpatterns = [
    path('d', views.VDashboardView, name = 'vdashboard'),
    path('report-filling', csrf_exempt(views.reportFillingView), name = 'report-filling'),
    path('rejected-report-filling', csrf_exempt(views.rejectedReportFillingView), name = 'rejected-report-filling'),
    path('sp', views.SetpasswordPageView, name = 'vresetpass'),
    path('profile', views.VProfileView, name = 'vprofile'),
    path('c', views.ChooseCoordinatorView, name = 'choose-coordinator'),
    path('v-download-certificate', views.downloadCertificateView, name = 'v-download-certificate'),
    path('v-download-report', views.downloadReportView, name = 'v-download-report'),
    path('v-request-to-update-email', views.VRequestToUpdateEmailView, name = 'v-request-to-update-email'),
    path('v-update-email/<str:new_email>/<str:current_email>', views.VUpdateEmailView, name = 'v-update-email'),
    path('mark_attendance', views.MarkAttendanceView, name='mark_attendance'),
    path('my_activity', views.my_activity, name='my_activity'),
    path('view_attendance', views.view_attendance, name='view_attendance'),
    path('fetch_attendance', views.fetch_attendance, name='fetch_attendance'),
    path('v_contact_us', views.v_contact_us, name='v_contact_us'),
    path('home_reportfilling', views.home_reportfilling, name='home_reportfilling'),
]