from django.shortcuts import render

def home(request):
    return render(request, 'ADA/home.html')

def lessons(request):
    return render(request, 'ADA/lessons.html')

def profile(request):
    return render(request, 'ADA/profile.html')

def trig(request):
    return render(request, 'ADA/trig.html')

def competitive(request):
    return render(request, 'ADA/competitive.html')

def leaderboard(request):
    return render(request, 'ADA/leaderboard.html')
