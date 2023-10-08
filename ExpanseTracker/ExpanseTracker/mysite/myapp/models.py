from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
# Create your models here.


class Expense(models.Model):
    def __str__(self):
        return self.name
    Username = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    name = models.CharField(max_length=100)
    amount = models.FloatField()
    category = models.CharField(max_length=50, choices=[
                                ("Housing", "Housing"), ("Transportation", "Transportation"), ("Personal Care", "Personal Care"), ("Taxes", "Taxes"), ("Food", "Food "), ("Healthcare", "Healthcare"), ("Utilities", "Utilities"), ("Fun", "Fun"), ("Gifts", "Gifts"), ("Home Supplies", "Home Supplies"), ("Clothes", "Clothes"), ("Other","Other")])
    date = models.DateField(auto_now=True)

    def get_absolute_url(self): # ??? -------
        return reverse('myapp:index', kwargs={})
