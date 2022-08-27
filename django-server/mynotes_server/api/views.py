from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializer

# Create your views here.


@api_view(["GET"])
def getRoutes(request):

    routes = [
        {
            'Endpoint': '/notes/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of notes'
        },
        {
            'Endpoint': '/notes/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single note object'
        },
        {
            'Endpoint': '/notes/create/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing note with data sent in post request'
        },
        {
            'Endpoint': '/notes/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes and exiting note'
        },
    ]

    return Response(routes)

@api_view(["GET"])
def getNotes(request):
    notes = Note.objects.all()
    # print("notes : ------------------------")
    # print(notes)
    serializer = NoteSerializer(notes, many = True)
    # print("serializer : ------------------------")
    # print(serializer.data)
    Json_note_Data =serializer.data 

    return Response(Json_note_Data)

@api_view(["GET"])
def getNote(request,pk):
    notes = Note.objects.get(id = pk)
    serializer = NoteSerializer(notes, many = False)
    Json_note_Data =serializer.data 
    
    return Response(Json_note_Data)
