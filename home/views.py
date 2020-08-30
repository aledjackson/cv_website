import django
from django.shortcuts import render
from django.http import HttpResponse
from .models import IntroAndProfilePic, LanguagesTools, Project
from django.core.serializers import serialize



# Create your views here.
def index(request) -> HttpResponse:
    introAndProfile = IntroAndProfilePic.objects.first()
    intro = introAndProfile.intro if introAndProfile is not None else ''
    profile_pic = str(introAndProfile.profile_pic) if introAndProfile is not None else ''
    languages = LanguagesTools.fetchAll()
    projects = Project.fetchAll()


    print(languages)

    return render(request, 'home/index.html', {"intro": intro, "profile_pic": profile_pic,
                                               "languages": languages, "projects": projects})

