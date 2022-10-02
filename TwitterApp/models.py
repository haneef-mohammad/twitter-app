from django.db import models

# Create your models here.

class Users(models.Model):
    UserId=models.IntegerField(primary_key=True)
    UserName=models.CharField(max_length=255)
    Follwers=models.CharField(max_length=255)
    CreatedOn=models.DateField()

class Tweets(models.Model):
    TweetId=models.IntegerField(primary_key=True)
    Tweet=models.CharField(max_length=1000)
    PostedBy=models.CharField(max_length=255)
    PostedOn=models.DateField()
