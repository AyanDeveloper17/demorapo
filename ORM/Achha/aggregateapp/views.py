from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .serializer import AuthorSerializer#PublisherSerializer,BookSerializer
from rest_framework.renderers import JSONRenderer
import json
# from django.utils.translation import gettext as _

# Create your views here.
def home(request):
    # author = Author.objects.get(id=id)
    author = Author.objects.all()
    serialize = AuthorSerializer(author,many=True)
    print(serialize)

    jsondata = JSONRenderer().render(serialize.data)
    print(jsondata)

    python = json.loads(jsondata) # converting to python objects
    print(python)

    convrt = json.dumps(python) # converting to json objects 
    print(convrt)

    return HttpResponse(python)#(request,'agt_index.html')

def table(request,id):
    auth = Author.objects.all()
    book_data = auth.book_set.get(id=id)
    data = {'book_data':book_data}    

    return render(request,'agt_table.html',data)

# def my_view(request):
#     data=['this, is, lazy, text']
#     output=_('|'.join(data))

#     return HttpResponse(output)