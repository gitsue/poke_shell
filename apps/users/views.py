from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def login_page(request):
	return render(request, "users/login.html")

def login(request):
	if request.method == "POST":
		user = User.objects.login(request.POST["user_name"])
		request.session["user_id"] = user.id

		return redirect("index")

	return redirect("login_page")

def logout(request):
	request.session.clear()
	return redirect("login_page")