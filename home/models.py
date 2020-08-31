from django.core.serializers import serialize
from django.db import models

# Create your models here.

# TODO: should probably limit the size of images that can be uploaded just in case

# no real use to use a db, I'm just being lazy here cause it doesn't matter
class IntroAndProfilePic(models.Model):
    intro = models.CharField(max_length=200)
    profile_pic = models.FileField(upload_to='user/images/profilepic/')
    def __str__(self):
        return self.intro


class LanguagesTools(models.Model):
    name = models.CharField(max_length=25)
    logo = models.FileField(upload_to='user/images/languages/')

    @staticmethod
    def fetchAll():
        querySet = LanguagesTools.objects.all()
        # json = dict(querySet)
        # return [{"name": rec["fields"]["name"], "logo": rec["fields"]["logo"]} for rec in json]
        return querySet

class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=400)
    image = models.FileField(upload_to='user/images/projects/')

    @staticmethod
    def fetchAll():
        querySet = Project.objects.all()
        return querySet


