from django.shortcuts import render, redirect
from ..users.models import User

# Create your views here.
def index(request):
	if "user_id" not in request.session:
		return redirect("login_page")

	context = {
		"curr_user": User.objects.get(id=request.session["user_id"])
	}

	return render(request, "pokes/index.html", context)