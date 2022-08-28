from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializer

# * /notes url (GET and POST) 

def getNotes (request):
    notes = Note.objects.all().order_by('-updated')
    # print("notes : ------------------------")
    # print(notes)
    serializer = NoteSerializer(notes, many = True)
    # print("serializer : ------------------------")
    # print(serializer.data)
    Json_note_Data =serializer.data 

    return Response(Json_note_Data)

def CreateNote(request):
    data = request.data
        # print(data)

    note = Note.objects.create(
        body = data["body"]
    )   

    serializer = NoteSerializer(note, many = False)
    Json_note_Data =serializer.data  
    
    return Response(Json_note_Data)

# * notes/<id> (GET,PUT,DELETE)
def getNote(request,pk):
    notes = Note.objects.get(id = pk)
    serializer = NoteSerializer(notes, many = False)
    Json_note_Data =serializer.data 
    
    return Response(Json_note_Data)


def updateNote(request,pk):
    data = request.data
    print(data)

    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(instance=note, data=data)

    if serializer.is_valid():
        serializer.save()

    Json_note_Data =serializer.data

    return Response(Json_note_Data)

def deleteNote(request,pk):
    note = Note.objects.get(id=pk)
    note.delete()
    return Response("Note was deleted!!!")
