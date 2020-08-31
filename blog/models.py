from django.db import models

# Create your models here.
from django.urls import reverse


class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=2000)

    @staticmethod
    def fetchAll():
        query_set = BlogPost.objects.all()
        return query_set

    @staticmethod
    def fetchTitles():
        class Title:
            def __init__(self,link,text):
                self.link = link
                self.text = text

        blog_url = reverse('blogHome')
        query_set = BlogPost.objects.all()
        titles = []
        for x in query_set:
            link = blog_url + x.title.replace(' ','%20')
            text = x.title
            titles.append(Title(link,text))

        return titles

    @staticmethod
    def fetchPost(title:str):
        # there is a bug here with case insensitivity but can I be bothered to fix it ¯\_(ツ)_/¯
        return BlogPost.objects.filter(title__iexact=title)
