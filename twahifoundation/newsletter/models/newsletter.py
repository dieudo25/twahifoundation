""" from django.db import models


class Subscriber(models.Model):


    class Meta:
       

    STATUS_CHOICES = [
        ('S', 'Subscribed'),
        ('P', 'Pending'),
        ('U', 'Unsubscribed'),
    ]

    email = models.EmailField(max_length=254)
    status = models.CharField(
        max_length=1,
        choices=STATUS_CHOICES,
    )
    subscribed_on = models.DateTimeField()

    def __str__(self):
        

        return f"{ self.email }"
 """
