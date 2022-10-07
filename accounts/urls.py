from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login_page, name='login'),

    # signup through email[OTP] - urls start
    path('signup/', signup, name='signup'),
    path('verify_registration_mail/', verify_registration_mail, name='verify_registration_mail'),
    path('registration_password_setter/', registration_password_setter, name='registration_password_setter'),
    # signup through email[OTP] - urls end

    # forgot password through email[OTP] - urls start
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('forgot_password_verify_otp/', forgot_password_verify_otp, name='forgot_password_verify_otp'),
    path('forgot_password_reset/', forgot_password_reset, name='forgot_password_reset'),
    # forgot password through email[OTP] - urls end

    path('logout/', logout_page, name='logout'),
]
