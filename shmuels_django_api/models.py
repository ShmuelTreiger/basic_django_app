from django.db import models


class Greetings(models.Model):
    greeting = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.greeting
