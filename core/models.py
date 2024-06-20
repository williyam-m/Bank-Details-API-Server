from django.db import models

# Create your models here.

class Bank(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Branch(models.Model):
    ifsc = models.CharField(max_length=11, primary_key=True)
    bank = models.ForeignKey(Bank, on_delete=models.CASCADE)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)

    def __str__(self):
        return f"{self.ifsc} - {self.bank} ({self.branch})"