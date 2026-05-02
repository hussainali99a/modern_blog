from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm, OTPForm, ProfileForm
from .models import EmailOTP


def landing_page(request):
    return render(request, "landing.html")


def send_otp_email(user):
    otp_obj = EmailOTP.objects.get(user=user)
    otp_obj.generate_otp()

    send_mail(
        subject="Verify your email - Modern Blog",
        message=f"""
Hello {user.username},

Your OTP for Modern Blog email verification is:

{otp_obj.otp}

This OTP is required to activate your account.

Thank you,
Modern Blog Team
""",
        from_email=None,
        recipient_list=[user.email],
        fail_silently=False,
    )

def register_view(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
            )
            user.is_active = False
            user.save()

            send_otp_email(user)

            request.session["verify_user_id"] = user.id
            messages.success(request, "Account created. Check console/email for OTP.")
            return redirect("accounts:verify_otp")
    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def verify_otp_view(request):
    user_id = request.session.get("verify_user_id")

    if not user_id:
        messages.error(request, "Session expired. Please register again.")
        return redirect("accounts:register")

    user = User.objects.get(id=user_id)
    otp_obj = EmailOTP.objects.get(user=user)

    if request.method == "POST":
        form = OTPForm(request.POST)

        if form.is_valid():
            entered_otp = form.cleaned_data["otp"]

            if entered_otp == otp_obj.otp:
                otp_obj.is_verified = True
                otp_obj.save()

                user.is_active = True
                user.save()

                login(request, user)
                messages.success(request, "Email verified successfully.")
                return redirect("blog:post_list")

            messages.error(request, "Invalid OTP.")
    else:
        form = OTPForm()

    return render(request, "accounts/verify_otp.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect("blog:post_list")
    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect("landing")


@login_required
def profile_view(request):
    profile = request.user.profile

    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)

        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("accounts:profile")
    else:
        form = ProfileForm(instance=profile)

    return render(request, "accounts/profile.html", {"form": form, "profile": profile})