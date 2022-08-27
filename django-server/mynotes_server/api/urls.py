from django.urls import path

from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('notes/' , view=views.getNotes,name = "notes"),
    path('notes/<str:pk>' , view=views.getNote,name = "note")
]
