from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth

# def login(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']

#         user = auth.authenticate(username=username, password=password)

#         if user is not None:
#             auth.login(request, user)
#             messages.success(request, 'You are now logged in')
#             return redirect('dashboard')
#         else:
#             messages.error(request, 'Invalid credentials')
#             return redirect('login')
#     else:
#         return render(request, 'accounts/login.html')

# def register(request):
#     if request.method == 'POST':
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         username = request.POST['username']
#         email = request.POST['email']
#         password = request.POST['password']
#         password2 = request.POST['password2']

#         if password == password2:
            
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, 'Username already exists')
#                 return redirect('register')
#             else:
#                 if User.objects.filter(email=email).exists():
#                     messages.error(request, 'Emails is being used')
#                     return redirect('register')
#                 else:
#                     user = User.objects.create_user(first_name=first_name,last_name=last_name,
#                     email=email,password=password, username=username)
#                     user.save()
#                     messages.success(request, 'Registration successful, proceed to Login')
#                     return redirect('login')
#         else:
#             messages.error(request, 'Passwords does not match')
#             return redirect('register')
#     return render (request, 'accounts/register.html')

# def logout(request):
#     if request.method == 'POST':
#         auth.logout(request)
#         messages.success(request, 'You are now logged out')
#         return redirect ('index')

def register(request):
    if request.method == "POST":
        phone = request.POST['phone']
        email = request.POST['email']
        password = request.POST['password']
        username = email.split('@')[0]

        if (email):
            user = CustomUser(username=username, email=email)
            user.set_password(password)
            user.save()
            return render(request, "accounts/login.html")
        else:
            error = True
            return render(request, 'accounts/register.html')
    else:
        return render(request, 'accounts/register.html') 

def login(request):
    if request.method == "POST":
        user_name = request.POST['username']
        password = request.POST['password']
        if "@" in user_name:
            user_name = user_name.split('@')[0]
        user = authenticate(request, username = user_name, password = password)
        
        if user is not None:
            login(request, user)
            return redirect("home:index")
        else:
            error_message = "yes"
            return render(request, "accounts/login.html")
    else:
        return render(request, "accounts/login.html")


def logout(request):
    logout(request)
    return redirect("login")