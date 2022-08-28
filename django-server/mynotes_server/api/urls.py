from django.urls import path

from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"),
    path('notes/' , view=views.NotesListPage,name = "notes"),
    # path('notes/create' , view=views.createNote,name = "create-note") ,
    # path('notes/<str:pk>/update' , view=views.updateNote,name = "update-note") ,
    # path('notes/<str:pk>/delete' , view=views.deleteNote,name = "delete-note") ,
    path('notes/<str:pk>' , view=views.NotePage,name = "note")
]
