from django.urls import path
from . import views
urlpatterns = [
    path('d', views.SecDashboardView, name='SDashboard'),
    path('sp', views.SetpasswordPageView, name='sresetpass'),
    path('ac', views.ApproveCoord, name='ApproveCoord'),
    path('rc', views.rejectCoordView, name='rejectCoord'),
    path('cd', views.coordDetailsView, name='coord-details'),
    path('va', views.viewVolunteerAttendanceView, name='view-volunteer-attendance'),
    path('a', views.s_my_activity, name='s_my_activity'),
    path('fv', views.failVolunteersView, name='fail-volunteers'),
    path('Certificate', views.showCertificate, name='s-show-certificate'),
    path('Report', views.showReport, name='s-show-report'),
    path('s-rf', views.ReportFillingSampleView, name='s-rf'),
    path('coord-reports', views.CoordReportsView, name='coord-reports'),
    path('download-attendance/', views.download_attendance, name='download_attendance'),
    path('add-event', views.addEventView, name='add-event'),
    path('show_events', views.show_events, name='show_events'),
    path('fetch-div/', views.activityDivisions, name='fetch_div'),
    path('updateEvent/', views.updateEvent, name='updateEvent'),
    path('deleteEvent/', views.deleteEvent, name='deleteEvent'),
    path('download-attendance/', views.download_attendance, name='download_attendance'),
    path('s_contact_us', views.s_contact_us, name='s_contact_us'),
]
