from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Customer
from django.db.models import Exists
from django.contrib import messages

# Create your views here.
def login(request):
    try:
        if request.method == 'POST':
            nm = request.POST.get('username')
            ps =request.POST.get('password')
    
           

            cust =Customer.objects.all()
            print(cust)
        
            
            for i in cust :
                names = i.customer_name
                password = i.customer_password
                if names == nm:
                    if password==ps:
                        return redirect('register')

                else:
                    return redirect('login')
             
    except Customer.DoesNotExist as a:
        messages.info(request,'user does not exists')

    return render(request,'index.html')

def register(request):
    if request.method == 'POST':
        nm = request.POST['name']
        em = request.POST['email']
        cnt = request.POST['contact']
        ps1 = request.POST['pass1']
        ps2 = request.POST['pass2']

        if ps1 == ps2:
            data = Customer(customer_name=nm,customer_email=em,customer_number=cnt,customer_password=ps1)
            data.save()
    return render(request,'register.html')

# def authenticate(request):
#     nm = request.POST.get('name')
#     ps = request.POST.get('pass1')
#     # user = Customer.objects.get(id=id)
#     user = Customer(customer_name=nm,customer_password=ps)
#     user.save()
#     if user==True:
#         return redirect('register')
#     elif user == None:
#         return redirect('login')
    
# def faltu(request):
#     context = [{'title':'Hello,Ayan!',
#     'para1':'This is a simple hero unit, a simple jumbotron-style component for calling extra attention to featured content or information.',
#     'para2':'It uses utility classes for typography and spacing to space content out within the larger container.',
#     'button':'learn here'}]
# ] 
#     content = {'context':context}
#     return render(request,'faltu.html',content)