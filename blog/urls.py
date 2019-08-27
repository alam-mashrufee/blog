from django.urls import path
from . import views

    urlpatters = [
        path('',view.post_list, name="post_list")
    ]