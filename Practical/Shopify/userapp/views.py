from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout,update_session_auth_hash
from .password_forgot import forgot_password
import uuid
from frontapp.models import Profile
from datetime import datetime, timedelta
import logging
from django.contrib.auth.decorators import login_required
from frontapp.models import Exceptions, UserActivity,Roleprofile
import socket
from userapp.serializers import RoleSerializer


## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)


logger = logging.getLogger(__name__)
date = datetime.now()


def save_exception_to_database(user_id, exception_code, exception_type, message, ip):
    user_id_instence = User.objects.get(id=user_id)
    exception_log = Exceptions(
        user_id=user_id_instence,
        exception_code=exception_code,
        exception_date=date,
        exception_type=exception_type,
        messages=message,
        IP=ip,
    )
    exception_log.save()


def track_user_activity(user, ip_address, description):
    activity = UserActivity(user_id=user, IP=ip_address, description=description)
    activity.save()

def login_user(request):
    try:
        if request.method == "POST":
            print(request.user)
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)

            try:
                if user is not None:
                    login(request, user)
                    request.session['username'] = username
                    request.session['is_logged_in'] = True
                    user_id_instence = User.objects.get(id=request.user.id)
                    description = {
                        "messages": "This user try to Login",
                        "data": request.POST,
                    }
                    activity = UserActivity(
                        user_id=user_id_instence,
                        IP=ip_address,
                        description=f"this is username {username} and {description}",
                    )
                    activity.save()
                    messages.success(request, "Login successful")

                    return redirect("product_list_page")

                else:
                    messages.success(request, "Invalid username or password")

                    return redirect("login")

            except Exception as e:
                print("Something went wrong")
                save_exception_to_database(
                    request.user.id, "40", type(e), str(e), ip_address
                )

    except Exception as e:
        print("some thing went wrong")
        save_exception_to_database(request.user.id, "40", type(e), str(e), ip_address)

    return render(request, "temp/login.html")


def logout_user(request):
    try:
        if request.user.is_authenticated:
            user_id_instence = User.objects.get(id=request.user.id)
            description = {"messages": "This user try to Logout", "data": request.POST}
            activity = UserActivity(
                user_id=user_id_instence,
                IP=ip_address,
                description=f"this is username {request.user.username} and {description}",
            )
            activity.save()
            logout(request)
            del request.session
            messages.success(request, "Logout successful")
            return redirect("login")

        else:
            return redirect("login")

    except Exception as e:
        print("something went wrong")
        save_exception_to_database(request.user.id, "40", type(e), str(e), ip_address)


def signup(request):
    try:
        if request.method == "POST":
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            
            user_obj = User.objects.create_user(
                username=username, email=email, password=password
            )
            profile_obj = Profile.objects.create(user=user_obj)
            profile_obj.save()
            role_obj = Roleprofile.objects.create(user=user_obj)
            role_obj.save()
        
            send_mail(
                "Your registration has been successfully Done Thanks for your registration",
                f"Welcome to Our App {username} Thanks for registration in app. ",
                "amandubey@simprosys.com",
                [email],
                fail_silently=False,
            )
            messages.success(
                request,
                "User registered successfully and please check your mail for confirmation",
            )
            return redirect("login")

        else:
            return render(
                request,
                "temp/registration.html",
            )
    except Exception as e:
        print("something went wrong", e)

        return render(
            request,
            "temp/registration.html",
        )


@login_required(login_url="login")
def change_password(request):
    if request.method == "POST":
        newpassword = request.POST.get("newpassword")
        if request.user.is_authenticated:
            user_id_instence = User.objects.get(id=request.user.id)
            description = {
                "messages": "This user try to changepassword",
                "data": request.POST,
            }
            activity = UserActivity(
                user_id=user_id_instence,
                IP=ip_address,
                description=f"this is username {request.user.username} and {description}",
            )
            activity.save()
            user = User.objects.get(username=request.user)
            user.set_password(newpassword)
            user.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Password has been changed sucssessfully")
            
            return redirect("/front/product_list_page")
        else:
            return redirect("/product_list_page")

    return render(request, "temp/changepassword.html")


def change_password_with_token(request, token):
    context = {}
    try:
        profile_obj = Profile.objects.filter(profile_token=token).first()
        print(profile_obj)
        date = datetime.now()
        exptime = int(datetime.timestamp(date))
        print("hereeeeeeeeeeeeeeeee")
        if profile_obj is not None and int(exptime) < int(profile_obj.time):
            if request.method == "POST":
                new_password = request.POST.get("newpassword")
                confirm_password = request.POST.get("confirmpassword")
                user_id = request.POST.get("user_id")
                print("hereeeeeeeeeeeeeeeeeee")
                if user_id is None:
                    messages.success(request, "User not found")

                    return redirect(f"change_password/{token}")

                elif new_password != confirm_password:
                    messages.success(request, "Both pasword are not the same")

                    return redirect(f"/front/change_password/{token}")

                user_obj = User.objects.get(id=user_id)
                user_obj.set_password(new_password)
                user_obj.save()
                messages.success(request, "Password has been changed successfully")

                return redirect("login")

            context = {"user_id": profile_obj.user.id}

        else:
            messages.success(request, "Link has been expired please try again")

            return redirect("forgot-password")

    except Exception as e:
        print("something went wrong")
        save_exception_to_database(request.user.id, "40", type(e), str(e), ip_address)

    return render(request, "temp/changepassword.html", context)



def forgot_password_with_email(request):
    try:
        if request.method == "POST":
            username = request.POST.get("username")
            if not User.objects.filter(username=username).first():
                messages.success(request, "User Not Found")

                return render(
                    request,
                    "temp/forgotpassword.html",
                )

            user_obj = User.objects.get(username=username)
            expiretime = datetime.now() + timedelta(hours=12)
            exptime = int(datetime.timestamp(expiretime))
            print(exptime)
            token = str(uuid.uuid4())
            profile_obj = Profile.objects.get(user=user_obj)
            profile_obj.profile_token = token
            profile_obj.time = exptime
            profile_obj.save()
            forgot_password(user_obj.email, token)
            # user_id_instence = User.objects.get(id=request.user.username)
            description = {
                "messages": "This user try to changepassword with forgotpassword",
                "data": request.POST,
            }
            activity = UserActivity(
                user_id=user_obj,
                IP=ip_address,
                description=f"this is username {request.user.username} and {description}",
            )
            activity.save()

            messages.success(request, "Forgot Password link has been sent on Email")

            return redirect("login")

    except Exception as e:
        print("something went wrong")
        save_exception_to_database(request.user.id, "40", type(e), str(e), ip_address)

    return render(
        request,
        "temp/forgotpassword.html",
    )


def Rolechange(request):
    if request.method =='POST':
        username = request.POST.get('username')
        is_admin = request.POST.get('is_admin')
        is_staff = request.POST.get('is_staff')
        user_obj = User.objects.filter(username = username).first()
        role_obj = Roleprofile.objects.filter(user = user_obj).first()
        if is_admin:
            role_obj.is_admin = True
            role_obj.is_staff = True
            role_obj.is_active = True
            role_obj.save()
            
            user_obj.is_superuser = True
            user_obj.is_staff = True
            user_obj.is_active = True
            user_obj.save()
        
        elif is_staff:
            role_obj.is_admin = False
            role_obj.is_staff = True
            role_obj.is_active = True
            role_obj.save()
            
            user_obj.is_superuser = True
            user_obj.is_staff = True
            user_obj.is_active = True
            user_obj.save()
        
        return redirect("admin_dashboard")
        
    else:
        return render(request,"temp/change_status.html")
from userapp.admin_requqired import admin_required_user

@admin_required_user
def admin_dashboard(request):
    roleprofile = User.objects.all()
    
    return render(request,"temp/admin_dashboard.html",{"data":roleprofile})

def admin_login(request):
    try:
        if request.method == "POST":
            print(request.user)
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)

            try:
                if user.is_superuser:
                    login(request, user)
                    request.session['username'] = username
                    request.session['is_logged_in'] = True
                    user_id_instence = User.objects.get(id=request.user.id)
                    description = {
                        "messages": "This user try to Login",
                        "data": request.POST,
                    }
                    activity = UserActivity(
                        user_id=user_id_instence,
                        IP=ip_address,
                        description=f"this is username {username} and {description}",
                    )
                    activity.save()
                    messages.success(request, "Login successful")

                    return redirect("admin_dashboard")

                else:
                    messages.success(request, "Invalid username or password")

                    return redirect("login")

            except Exception as e:
                print("Something went wrong")
                save_exception_to_database(
                    request.user.id, "40", type(e), str(e), ip_address
                )

    except Exception as e:
        print("some thing went wrong")
        save_exception_to_database(request.user.id, "40", type(e), str(e), ip_address)

    return render(request, "temp/login.html")


def user_delete(request,pk):
    user = User.objects.get(id = pk)
    print(user)
    user.delete()
    return redirect("admin_dashboard")

def update_user(request,pk):
    user_obj = User.objects.get(id=pk)
    print(user_obj)
    if request.method=="POST":
        username = request.POST.get('username')
        is_admin = request.POST.get('is_admin')
        is_staff = request.POST.get('is_staff')
        is_active = request.POST.get('is_active')
        user_obj.username = username
        user_obj.is_superuser = is_admin
        user_obj.is_staff = is_staff
        user_obj.is_active = is_active
        user_obj.save()
        return redirect("admin_dashboard")
    
    return render(request,"temp/update_user.html",{"user_obj":user_obj})
    
        