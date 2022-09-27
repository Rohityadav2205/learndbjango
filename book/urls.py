from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index),
    path("allbooks/", views.allbooks),
    path("between/", views.between),
    path("searchbooks/", views.searchbooks),
    path("searchor/", views.searchor),
    path("aggregates/", views.aggregates),
    path("subject/", views.subject),
    path("user/", views.user),
]
