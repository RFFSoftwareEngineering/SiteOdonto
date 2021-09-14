from django.shortcuts import render, redirect
from datetime import datetime

now = datetime.now().strftime('%H:%M:%S')


def HomePage(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    now = datetime.now().strftime('%H:%M:%S')
    context = {
            "actual_time": now
        }
    return render(request, "home.html", context)
