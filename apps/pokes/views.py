from django.shortcuts import render, redirect
from ..users.models import User
from .models import Poke
from django.db.models import Sum

# Create your views here.
def index(request):
	if "user_id" not in request.session:
		return redirect("login_page")

	context = {
		"curr_user": User.objects.get(id=request.session["user_id"]),
		"users": User.objects.exclude(id=request.session["user_id"]).annotate(total_count=Sum("pokee__count")),
	}

	return render(request, "pokes/index.html", context)

def poke(request, pokee_id):
	Poke.pokemgr.add_poke(request.session["user_id"], pokee_id)

	return redirect("index")

