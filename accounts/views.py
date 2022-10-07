# This Django app is build for automation using python, build by Abhijith KR 

from django.shortcuts import redirect, render

# importing django login athentications
from django.contrib.auth import authenticate, login, logout

from accounts.models import User_Account

from django.contrib.auth.models import User

import random # it is for otp generating purpose

# email sending purpose
from django.template.loader import render_to_string # email html setup purpose
from django.core.mail import EmailMessage # Email sending purpose
from django.conf import settings 

# Create your views here.

# index
def index(request):
    if request.user.is_authenticated: 
        print(request.user,'User already logged in')
        return render(request,'admin/dashboard.html')
    else:
        return render(request,'index.html')
# signup
def signup(request):

    # user already logged in section (case 1)
    if request.user.is_authenticated: 
        print(request.user,'User already logged in')
        return render(request,'admin/dashboard.html')

    else:
        # Registration section (case 2)
        if request.method == 'POST':
            email = request.POST.get('email')
            # pswd1 = request.POST.get('pswd1')
            # pswd2 = request.POST.get('pswd2')
    
            # print(email)
            # print(pswd1)
            # print(pswd2)

            if(email== ''):
                print('No value')
                context={'static_mail':email,'error_msg':'Please enter valid info...'}
                return render(request,'accounts/signup.html',context)

            # check email exist or not 
            elif User.objects.filter(username=email).exists():
                context={'static_mail':email,'error_msg':'Email already registered'}
                return render(request,'accounts/signup.html',context)

            else:

                username=email[:-(len('@gmail.com'))]
                print(username,'username')

                otp = str(random.randint(10000 , 99999))# random otp generator
                print(otp)
                # saving email, otp, verification string in session for verify and after save data to database using (verify function)
                request.session['email'] = email
                request.session['otp'] = otp
                request.session['verification'] = 'verify' #verification is a checker session_key

                # mail sending code area
                mydict={'username':username,'otp':otp}
                html_template = 'email_templates/registration_or_forgot_psd_sender.html'
                html_message = render_to_string(html_template, context=mydict)
                subject = 'Verification Code For Registration'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [email]
                message = EmailMessage(subject, html_message, email_from, recipient_list)
                message.content_subtype = 'html'
                message.send()
                print('email send successfully')

                print('verify mail')
                return redirect('verify_registration_mail')

            # elif(len(pswd1)<6):
            #     print('Password length too short.')
            #     context={'static_mail':email,'error_msg':'Password length is too short. Require a minimum password length of 6–10 characters.'}
            #     return render(request,'accounts/signup.html',context)

            # elif(not pswd1==pswd2):
            #     print('Password Missmatch')
            #     context={'static_mail':email,'error_msg':"Those passwords didn't match. Try again."}
            #     return render(request,'accounts/signup.html',context)

            # elif User.objects.filter(username=email).exists():
            #     print('User already exist View')
            #     context={'static_mail':email,'error_msg':'Email already exist...'}
            #     return render(request,'accounts/signup.html',context)

            # else:
            #     User_db=User.objects.create_user(
            #             username=email,
            #             password=pswd1,
            #         )
            #     # user_obj.set_password(password)

            #     User_Account.objects.create(
            #         user_id=User_db,
            #         email=email,
            #     )

                # print('Sucessfully registered')
                # return render(request,'accounts/login.html',{'success_msg': 'Successfully registered, Please login','static_mail':email})
                    
        return render(request,'accounts/signup.html')

# signup - sub view
# verify_registration_mail - otp validator
def verify_registration_mail(request):
    email=request.session.get('email')
    otp=request.session.get('otp')
    verification=request.session.get('verification')
    print(email)
    print(otp)
    print(verification)


    if not request.session.get('verification') == 'verify':
        return redirect('/')
    else:
        if request.method == 'POST':
            form_otp = request.POST.get('otp')
            print(otp)

            if otp == form_otp:
                print('verified')
                request.session['verification'] = 'set_password' #verification is a checker session_key
                return redirect('registration_password_setter')
            else:
                print('wrong verification code')
                context = {'email':email,'msg':'Wrong verification code', 'form_otp': form_otp}
                return render(request,'accounts/verify_registration_mail.html',context)

    context={'email':email}
    return render(request,'accounts/verify_registration_mail.html', context)

# signup - sub view
# registration_password_setter - saving email and password to database(last stage of registration)
def registration_password_setter(request):
    email=request.session.get('email')


    if not request.session.get('verification') == 'set_password':
        return redirect('/')
    else:
        if request.method == 'POST':
            psd = request.POST.get('psd')
            confirm_psd = request.POST.get('confirm_psd')
            print(email)
            print(psd)
            print(confirm_psd)


            if not psd == confirm_psd:
                print('password not match')
                context = {'msg':'Password does not match'}
                return render(request,'accounts/registration_password_setter.html', context)

            else:
                user_db=User.objects.create(username=email)
                user_db.set_password(psd)
                user_db.save()

                User_Account.objects.create(
                    user_id=user_db,
                    email=email,
                )
                # request.session['verification'] = False
                request.session.flush() # deleting all registration session from database
                print('User verified and created')
                context = {'success_msg': 'Successfully registered, Please login','static_mail':email}
                return render(request,'accounts/login.html',context)

    context={}
    return render(request,'accounts/registration_password_setter.html', context)

def login_page(request):
    # user already logged in section (case 1)
    if request.user.is_authenticated: 
        print(request.user,'User already logged in')

        return render(request,'admin/dashboard.html')
    
    else:
        # Login section (case 2)
        if request.method == 'POST':
            email = request.POST.get('email')
            pswd = request.POST.get('pswd')

            # print(email)
            # print(pswd)


            if(email== '' or pswd==''):
                print('No value')
                context={'static_mail':email,'error_msg':'Please enter valid info...'}
                return render(request,'accounts/login.html',context)

            else:
                user =authenticate(request, username=email, password=pswd) # check the user is valid
                print(user)

                if user is not None:
                    login(request, user) #login is hold uservalue(request&user), and added to django_section database
                    print(type(user),user)
                    print('User Login succesfull')

                    return render(request,'admin/dashboard.html')   

                else:
                    print(user,'user')
                    print('login failed')
                    context={'static_mail':email,'error_msg':'Invalid Email and Password'}
                    return render(request,'accounts/login.html',context)

        return render(request,'accounts/login.html')

def logout_page(request):
    logout(request)
    return redirect('/')

# Forgot Password logic
def forgot_password(request):
    if request.method=='POST':
        email=request.POST.get('email')
        print(email)

        if User.objects.filter(username=email).exists():
            print('email exist')

            # username fetching
            # User_db=User.objects.get(username=email)
            # if User_db.extend_usermodel.role == 'recruiter':
            #     username=User_db.recruiter.company_name
            # else:
            #     username=User_db.candidate.name
            # print(username,'??????????????????????')
            
            # or

            username=email[:-(len('@gmail.com'))]
            print(username,'username')

            otp = str(random.randint(10000 , 99999))# random otp generator
            print(otp)
            # saving email and otp in session for verify and after resetting password
            request.session['email'] = email
            request.session['otp'] = otp
            request.session['verification'] = 'verify' #verification is a checker session_key(if a view(verify_otp,password_reset) is valid or not)
            
            # email sending area
            mydict={'username':username,'otp':otp}
            html_template = 'email_templates/registration_or_forgot_psd_sender.html'
            html_message = render_to_string(html_template, context=mydict)
            subject = 'Password Reset Verification Code'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [email]
            message = EmailMessage(subject, html_message, email_from, recipient_list)
            message.content_subtype = 'html'
            message.send()
            print('email send successfully')

            return redirect('forgot_password_verify_otp')

        else:
            print('email does not exist')
            context = {'static_mail':email, 'error_msg':"Email doesn't exist"}
            return render(request,'accounts/forgot_password.html', context)

    return render(request,'accounts/forgot_password.html')

# Forgot Password - sub view
def forgot_password_verify_otp(request):
    email=request.session.get('email')
    otp=request.session.get('otp')
    verification=request.session.get('verification')
    # print(request.session.get('email'),'session')
    # print(request.session.get('otp'),'session')
    # print(request.session.get('verification'),'session')

    if not verification == 'verify':
        return redirect('/')

    else:
        if request.method == 'POST':
            form_otp = request.POST.get('otp')
            print(otp)

            if otp == form_otp:
                print('verified')
                request.session['verification'] = 'set_password' #verification is a checker session_key
                return redirect('forgot_password_reset')
            else:
                print('wrong verification code')
                context = {'email':email,'msg':'Wrong verification code', 'form_otp': form_otp}
                return render(request,'accounts/forgot_password_verify_otp.html', context)

    return render(request,'accounts/forgot_password_verify_otp.html', {'email':email})

# Forgot Password - sub view
def forgot_password_reset(request):
    email=request.session.get('email')
    verification=request.session.get('verification')

    if not verification == 'set_password':
        return redirect('/')

    else:
        if request.method == 'POST':
            psd = request.POST.get('psd')
            confirm_psd = request.POST.get('confirm_psd')
            # print(psd)
            # print(confirm_psd)

            if(len(psd)<6):
                print('Password length too short.')
                context = {'msg':'Password must have at least 6 characters', 'psd':psd,'confirm_psd':confirm_psd}
                return render(request,'accounts/forgot_password_reset.html', context)

            elif not psd == confirm_psd:
                print('Password must be same')
                context = {'msg':'Password does not match', 'psd':psd,'confirm_psd':confirm_psd}
                return render(request,'accounts/forgot_password_reset.html', context)       

            else:
                if User.objects.filter(username=email).exists():
                    User_db=User.objects.get(username=email)
                    # print(User_db.password)
                    # print(User_db.username)

                    User_db.set_password(psd)
                    User_db.save()
                    print('Password reset successfully')
                    request.session.flush() # deleting all forgot_password_reset session from "database and browser"
                    # return redirect('login')
                    context = {'success_msg': 'Password changed Successfully, Please login','static_mail':email}
                    return render(request,'accounts/login.html',context)

                else:
                    return redirect('/')
        

    return render(request,'accounts/forgot_password_reset.html',{})