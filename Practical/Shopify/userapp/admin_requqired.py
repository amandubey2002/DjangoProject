from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect
from django.http import HttpResponseForbidden

def admin_required_user(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.user.is_superuser:
            return redirect("login")
        return view_func(request, *args, **kwargs)
    return wrapper