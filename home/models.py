from django.db import models

# Create your models here.

# no real use to use a db, I'm just being lazy here cause it doesn't matter
class IntroAndProfilePic(models.Model):
    intro = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='user/images/profilepic/')

    def __str__(self):
        return self.intro

class LanguagesTools(models.Model):
    item = models.CharField(max_length=25)
    logo = models.ImageField(upload_to='user/images/languages/')

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.charField(max_length=400)
    image = models.ImageField(upload_to='user/images/projects/')


def intro():
    i = """Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    Ut enim ad minim veniam, quis """

    return i

