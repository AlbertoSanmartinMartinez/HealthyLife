from django.db.models.signals import post_save
from django.dispatch import receiver
from healthylifeapp import models

@receiver(post_save, sender=models.Post)
def createPost(sender, **kwargs):
    pass
