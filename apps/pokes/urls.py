from django.conf.urls import url
from . import views

urlpatterns = [
	url(r"^$", views.index, name="index"),
	url(r"^poke(?P<pokee_id>\d+)$", views.poke, name="add_poke"),
]