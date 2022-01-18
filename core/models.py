from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.db.models.signals import post_delete
from django.dispatch import receiver


def upload_location(instance, filename):
    file_path = 'profile/{user}/{filename}'.format(
         user=str(instance.user), filename=filename)
    return file_path


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=50, blank=True, null=True)
    profile_image = models.FileField(upload_to=upload_location, blank=True, null=True)
    dob = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.user.username)


@receiver(post_delete, sender=Profile)
def submission_delete(sender, instance, **kwargs):
    instance.profile_image.delete(False)


def pre_save_profile_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(str(instance.user.username) + "-" + str(instance.user.id))


pre_save.connect(pre_save_profile_receiver, sender=Profile)


