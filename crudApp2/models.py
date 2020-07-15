from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Book(models.Model):
    name = models.CharField(max_length = 50)
    picture = models.ImageField(upload_to="images/")
    author = models.CharField(max_length = 30)
    email = models.EmailField()
    describe = models.TextField()
    def __str__(self):
        return self.name

    class Meta:
        db_table = "book"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    # other fields...

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
