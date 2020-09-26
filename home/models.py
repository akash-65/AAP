from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Member(models.Model):
    Sr_No = models.AutoField(primary_key=True)

    ROLE_OPTIONS = (
        ('Alumni', 'Alumni'),
        ('Student', 'Student'),
    )

    BRANCH_OPTIONS = (
        ('Computer Science', 'Computer Science'),
        ('Electronics & Telecommunication', 'Electronics & Telecommunication'),
        ('Mechanical Engineering', 'Mechanical Engineering'),
        ('Civil Engineering', 'Civil Engineering'),
        ('Chemical Engineering', 'Chemical Engineering'),
        ('Others', 'Others'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True, )
    Role = models.CharField(max_length=100, choices=ROLE_OPTIONS, null=True, blank=True, default='NA')
    Graduation_Starting_Year = models.IntegerField(null=True, blank=True, default=0)
    Graduation_Ending_Year = models.IntegerField(null=True, blank=True, default=0)
    Branch = models.CharField(max_length=100, choices=BRANCH_OPTIONS, null=True, blank=True, default='NA')
    PRN_No = models.IntegerField(blank=True, null=True, default=0)
    Final_CGPA = models.IntegerField(blank=True, null=True, default=0)
    Mobile_No = models.CharField(max_length=100, null=True, blank=True, default=0)
    Profile_Photo = models.ImageField(upload_to="Static/home", default="media/Static/home/dypiemr.jpg", blank=True,
                                      null=True)
    Bio = models.CharField(max_length=1000, blank=True, null=True, default='NA')
    Job = models.CharField(max_length=500, blank=True, null=True, default='NA')
    Project = models.CharField(max_length=500, blank=True, null=True, default='NA')
    Technical_Skills = models.CharField(max_length=500, blank=True, null=True, default='NA')
    Hobbies = models.CharField(max_length=500, blank=True, null=True, default='NA')
    Time = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name + ' | ' + self.Role


class Contact(models.Model):
    Sr_No = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.CharField(max_length=50, blank=True)
    number = models.CharField(max_length=20, blank=True)
    message = models.TextField()
    Time = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.fname + " " + self.lname
