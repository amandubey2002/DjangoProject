from django.core.mail import send_mail


def forgot_password(email,token):
    send_mail("Forgot Password link...",
                    f"Click on the link for change your password. http://127.0.0.1:8000/user/change_password/{token} ",
                    "amandubey@simprosys.com",
                    [email],
                    fail_silently=False,
                )
    return True