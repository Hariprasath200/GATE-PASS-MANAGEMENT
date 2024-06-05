from django.contrib.auth.models import AbstractUser
from django.db import models

class Std(models.Model):
    PENDING = 'PENDING'
    ACCEPTED = 'ACCEPTED'
    REJECTED = 'REJECTED'

    STATUS_CHOICES = [
        (PENDING, 'PENDING'),
        (ACCEPTED, 'ACCEPTED'),
        (REJECTED, 'REJECTED'),
    ]
    HOD_STATUS_CHOICES = [
        (PENDING, 'PENDING'),
        (ACCEPTED, 'ACCEPTED'),
        (REJECTED, 'REJECTED'),
    ]
    student_name = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=50)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=15)
    description = models.TextField()
    incharge_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    hod_status = models.CharField(max_length=10, choices=HOD_STATUS_CHOICES, default=PENDING)
    parent_name = models.CharField(max_length=100)
    parent_number = models.CharField(max_length=15)
    department = models.CharField(max_length=100)


from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    USER_ROLES = (
        ('student', 'student'),
        ('incharge', 'incharge'),
        ('hod', 'hod'),
        ('warden', 'warden'),
        ('security', 'security'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=USER_ROLES)
