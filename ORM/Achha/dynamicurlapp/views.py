from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):

    return render(request,'index.html')


def dynamic(request,ayan_id):
    print(ayan_id)
    data = {
        'ayan_id':ayan_id,'name':'Ayan'
    }
    return render(request,'dynamic_url.html',data)

def converter(request,pk=1):
    print(pk)
    if pk == 3:   
        data2 = {'pk':pk}
    return render(request,'dynamic_url.html',data2)

def doubleid(request,a_id,y_id):
    if a_id == 12 and y_id == '1':
        data2 = {'a_id':a_id,
                 'y_id':y_id
        }
    return render(request,'dynamic_url.html',data2)
