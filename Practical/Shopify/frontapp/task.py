from celery import shared_task
from django.contrib.auth.models import User
from django.core.mail import send_mail
from frontapp.celery import app
from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect


@shared_task(bind=True)
def send_mail_to_user(self):
    users = User.objects.all()
    print(users)
    for user in users:
        send_mail(
            "Hey There",
            f" Hey {user.username}, Happy Birthday! On this special day, I wish you a year filled with joy, laughter, and love. May all your dreams come true and may you achieve success in all your endeavors. May you be surrounded by your loved ones, and may your heart be filled with gratitude and appreciation for the blessings in your life. May you continue to grow, learn, and become the best version of yourself. Wishing you a fantastic birthday and an amazing year ahead! Cheers to another trip around the sun!",
            "amandubey@simprosys.com",
            [user.email],
            fail_silently=False,
        )
    messages = "Send Email Successfully"
    
    return redirect("home", messages=messages)
