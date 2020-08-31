from django.urls import path
from . import views

urlpatterns = [
    path('blog/', views.blogHome, name='blogHome'),
    path('blog/<str:title>', views.blogPost, name='blogPost')
]