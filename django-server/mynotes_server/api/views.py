import re

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializer
from .utils import *

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
        # {
        #     'Endpoint': '/notes/create/',
        #     'method': 'POST',
        #     'body': {'body': ""},
        #     'description': 'Creates new note with data sent in post request'
        # },
        # {
        #     'Endpoint': '/notes/id/update/',
        #     'method': 'PUT',
        #     'body': {'body': ""},
        #     'description': 'Creates an existing note with data sent in post request'
        # },
        # {
        #     'Endpoint': '/notes/id/delete/',
        #     'method': 'DELETE',
        #     'body': None,
        #     'description': 'Deletes and exiting note'
        # },
    ]

    return Response(routes)


# * for notes url

# @api_view(["GET"])
# def getNotes(request):
#     notes = Note.objects.all().order_by('-updated')
#     # print("notes : ------------------------")
#     # print(notes)
#     serializer = NoteSerializer(notes, many = True)
#     # print("serializer : ------------------------")
#     # print(serializer.data)
#     Json_note_Data =serializer.data 

#     return Response(Json_note_Data)

# @api_view(["POST"])
# def createNote(request):
#     data = request.data
#     # print(data)

#     note = Note.objects.create(
#         body = data["body"]
#     )   

#     serializer = NoteSerializer(note, many = False)
#     Json_note_Data =serializer.data  
    
#     return Response(Json_note_Data)

# * for notes/<id> url 

# @api_view(["GET"])
# def getNote(request,pk):
#     notes = Note.objects.get(id = pk)
#     serializer = NoteSerializer(notes, many = False)
#     Json_note_Data =serializer.data 
    
#     return Response(Json_note_Data)

# @api_view(["PUT"])
# def updateNote(request , pk):
#     data = request.data
#     print(data)

#     note = Note.objects.get(id=pk)
#     serializer = NoteSerializer(instance=note, data=data)

#     if serializer.is_valid():
#         serializer.save()

#     Json_note_Data =serializer.data

#     return Response(Json_note_Data)

# @api_view(["DELETE"])
# def deleteNote(request,pk):
#     note = Note.objects.get(id=pk)
#     note.delete()
#     return Response("Note was deleted!!!")


# * Now we try to turn the api to RESTful API 
# Meaning that we only have 2 API , but 5 endpoint 

# /notes GET
# /notes POST 

# /notes/<id> GET
# /notes/<id> PUT 
# /notes/<id> DELETE


# * /notes url (GET and POST) 

@api_view(["GET","POST"])
def NotesListPage(request):

    if request.method == "GET":
        return getNotes (request)
        # notes = Note.objects.all().order_by('-updated')
        # # print("notes : ------------------------")
        # # print(notes)
        # serializer = NoteSerializer(notes, many = True)
        # # print("serializer : ------------------------")
        # # print(serializer.data)
        # Json_note_Data =serializer.data 

        # return Response(Json_note_Data)

    if request.method == "POST":  # Create note 
        return CreateNote(request)
        # data = request.data
        # # print(data)

        # note = Note.objects.create(
        #     body = data["body"]
        # )   

        # serializer = NoteSerializer(note, many = False)
        # Json_note_Data =serializer.data  
        
        # return Response(Json_note_Data)


# * notes/<id> (GET,PUT,DELETE)

@api_view(["GET","PUT","DELETE"])
def NotePage(request,pk):

    # GET note
    if request.method == "GET": 
        return getNote(request,pk)
        # notes = Note.objects.get(id = pk)
        # serializer = NoteSerializer(notes, many = False)
        # Json_note_Data =serializer.data 
        
        # return Response(Json_note_Data)

    if request.method == "PUT": # update Note
        return updateNote(request,pk)
        # data = request.data
        # print(data)

        # note = Note.objects.get(id=pk)
        # serializer = NoteSerializer(instance=note, data=data)

        # if serializer.is_valid():
        #     serializer.save()

        # Json_note_Data =serializer.data

        # return Response(Json_note_Data)

    if request.method == "DELETE": # Delete note
        return deleteNote(request,pk)
        # note = Note.objects.get(id=pk)
        # note.delete()
        # return Response("Note was deleted!!!")
