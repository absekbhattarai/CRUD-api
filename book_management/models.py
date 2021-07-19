from django.db import models

class book(models.Model):
    name = models.CharField(max_length=200)
    ISBN_number = models.IntegerField()

    def __str__(self):
        return self.name

