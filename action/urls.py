from django.urls import path
from . import views
urlpatterns = [
    path('download-volunteer-reports', views.downloadVolunteerReportView, name='downloadVolunteerReportView'),
    path('download-coordinator-reports', views.downloadCoordinatorReportView, name='downloadCoordinatorReportView'),
    path('allot', views.allotCoordinatorSequentialView, name='allot'),
    path('allot-coords-by-sheet', views.allotCoordsBySheet, name='allot-coords-by-sheet'),
    path('download-volunteer-certificates-zip', views.downloadVolunteerCertificatesZip, name='download-volunteer-certificates-zip'),
    path('generate-individual-certificate', views.generateIndividualCertificate, name='generate-individual-certificate'),
    path('test', views.testCertificateView, name='test-certificate'),
    path('fail', views.failVolunteerView, name='fail'),
    path('run-function', views.runFunction),
    path('send-email', views.sendEmailView, name='send-email'),
    path('info', views.infoView, name='info'),
    path('fetch-volunteer-names', views.fetchVolunteerNames),

    path('', views.verifyAdmin, name='verifyAdmin'),
    path('deleteVol/', views.deleteVolunteer, name='deleteVol'),
    path('onlyVolunteer/', views.onlyVolunteer, name='deleteOnlyVolunteer'),
    path('viewVolunteer/', views.viewVolunteer, name='viewVolunteer'),
    path('deleteAttendance/', views.deleteAttendance, name='deleteAttendance'),
    path('coordAttendance/', views.coordAttendance, name='coordAttendance'),
]