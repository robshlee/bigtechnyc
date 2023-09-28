from django.db import models
from django.contrib.auth.models import User as DjangoUser

class Company(models.Model):
    name = models.CharField(max_length=100)

class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    job_link = models.URLField()
    created_timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

class User(models.Model):
    email = models.EmailField(unique=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    AUTH_METHOD_CHOICES = (
        ('google', 'Google'),
        ('github', 'GitHub'),
    )
    auth_method = models.CharField(max_length=10, choices=AUTH_METHOD_CHOICES)

class UserJob(models.Model):
    user = models.ForeignKey(DjangoUser, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    saved_timestamp = models.DateTimeField(auto_now_add=True)
    applied_timestamp = models.DateTimeField(null=True, blank=True)
