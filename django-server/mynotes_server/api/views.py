
from rest_framework.decorators import api_view
from rest_framework.response import Response


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
    ]

    return Response(routes)



# * RESTful API 
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

    if request.method == "POST":  # Create note 
        return CreateNote(request)


# * notes/<id> (GET,PUT,DELETE)

@api_view(["GET","PUT","DELETE"])
def NotePage(request,pk):

    # GET note
    if request.method == "GET": 
        return getNote(request,pk)

    if request.method == "PUT": # update Note
        return updateNote(request,pk)

    if request.method == "DELETE": # Delete note
        return deleteNote(request,pk)

