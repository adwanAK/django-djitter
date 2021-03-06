from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Djteerprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    follows = models.ManyToManyField('self', related_name='followed_by', symmetrical = False)

    user.djeeterprofile = property(lambda u: DjeeterProfile.objects.get_or_create(user=u)[0])

