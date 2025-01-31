from django.urls import path
from . import views_registration, views_authentication
urlpatterns = [
    path('v', views_registration.VolunteerRegistrationView, name='vreg'),
    path('c', views_registration.CoordRegistrationView, name='creg'),
    path('s', views_registration.SecretaryRegistrationView, name='sreg'),
    path('login', views_authentication.LoginView, name='login'),
    path('login-restricted', views_authentication.LoginRestrictedView),
    path('logout', views_authentication.LogoutView, name='logout'),
    path('r', views_authentication.RequestPasswordResetEmail, name='reset'),
    path('snp/<uidb64>/<token>', views_authentication.SetNewPasswordView, name='setnewpassword'),
]