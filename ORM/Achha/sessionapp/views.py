from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name'] = 'Ayan'
    request.session['lname'] ='Shaikh'
    return render(request,'set_session.html')

def getsession(request):
#    name = request.session['name']
    name = request.session.get('name',default='Oops! Your Session has been deleted...')
    lname = request.session.get('lname',default='')
    return render(request,'get_session.html',{'name':name,'lname':lname})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
        del request.session['lname']
    return render(request,'del_session.html')
    