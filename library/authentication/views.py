# Create your views here.
from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser

# Реєстрація нового користувача
def register(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")

        if email and password:
            user = CustomUser.objects.create(email=email, password=password, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()
            return JsonResponse({"message": "User created successfully!"})
        return JsonResponse({"error": "Please provide all necessary fields."}, status=400)

    return render(request, "register.html")

# Аутентифікація користувача
def login_user(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return JsonResponse({"message": "Login successful!"})
        return JsonResponse({"error": "Invalid credentials."}, status=400)

    return render(request, "login.html")

# Вихід користувача
def logout_user(request):
    logout(request)
    return JsonResponse({"message": "Logout successful!"})
