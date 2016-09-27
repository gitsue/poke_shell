from django.db import models
from ..users.models import User

# Create your models here.

class PokeManager(models.Manager):
	def add_poke(self, poker_id, pokee_id):
		poker = User.objects.get(id=poker_id)
		pokee = User.objects.get(id=pokee_id)

		poke = self.filter(pokee=pokee, poker=poker)
		if poke:
			poke[0].count +=1
			poke[0].save()
		else:
			self.create(pokee=pokee, poker=poker, count=1)


class Poke(models.Model):
	poker = models.ForeignKey(User, related_name="poker")
	pokee = models.ForeignKey(User, related_name="pokee")
	count = models.IntegerField(default=0)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now_add=True)
	pokemgr = PokeManager()	