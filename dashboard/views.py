from django.shortcuts import render

def login(request):
    return render(request, "login.html")

def dashboard(request):
    return render(request, "dashboard.html")

def users(request):
    return render(request, "users.html")

def products(request):
    return render(request, "products.html")

def orders(request):
    return render(request, "orders.html")

def reports(request):
    return render(request, "reports.html")

def settings(request):
    return render(request, "settings.html")

def profile(request):
    return render(request, "profile.html")