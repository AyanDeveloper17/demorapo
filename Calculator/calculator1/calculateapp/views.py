from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
def calculate(request):
    try:
        if request.method =='POST':
            user = request.POST.get('user')
            print(user)
            oprate = request.POST.get('opr')
            print(oprate)

            
            # if user==user:
            #     user = request.POST.get('user')
            # elif oprate==oprate:
            #     oprate = request.POST.get('opr')
            
            

            if oprate=='+':
                a = (user + user)
            
            elif oprate=='-':
                b = (user - user)
                
            elif oprate=='*':
                c = (user * user)
            
            elif oprate=='/':
                d = (user / user)
            
            elif oprate=='square':
                e = (user ** 2)
                
            elif oprate == 'cube':
                f = (user ** 3 )
            
            elif (oprate != '+' and oprate!='-' and oprate!='*' and oprate!= '/' and oprate!= 'square' and oprate !='cube'):
                pass
            return render(request,'calculate.html')
    except:
        # messages.info(request,'Error occurd')
        pass
            
    return render(request,'calculate.html')
