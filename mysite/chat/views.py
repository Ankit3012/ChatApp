from django.shortcuts import render, HttpResponse, redirect
from .models import userlogin,Messages
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
import random
from uuid import getnode as get_mac
# Create your views here.
@csrf_exempt
def index(request):
    mac = get_mac()
    if request.method == 'POST':
        if request.POST.get('email'):
            email = request.POST.get('email')
            password = request.POST.get('pass')
            try:
                dbemail = userlogin.objects.get(email=email).email
                dbname = userlogin.objects.get(email=email).name
                dbpass = userlogin.objects.get(email=email).password
                uid = userlogin.objects.get(email=email).userid

                if str(dbemail) == str(email) and str(dbpass) == password:
                    all = userlogin.objects.all()
                    return render(request, 'chat.html', {'owner':str(dbname),'all': all,
                                                         'username': uid,'receiver':'User'})
            except:
                return render(request, 'login.html')
        elif request.POST.get('remail'):
            name = request.POST.get('name')
            email = request.POST.get('remail')
            password = request.POST.get('pass')
            repassword = request.POST.get('repass')

            r1 = random.randint(0, 99999)
            newid = r1 + 3012 + mac
            print(newid)
            if password==repassword:
                b2 = userlogin(userid=int(newid),name=name, email=email,password=str(password),access = True)
                b2.save()
    return render(request, 'login.html')



@csrf_exempt
def chat(request,sender,receiver):

    all = userlogin.objects.all()
    em=userlogin.objects.get(userid=int(receiver)).email
    r_name=userlogin.objects.get(userid=int(receiver)).name
    s_name = userlogin.objects.get(userid=int(sender)).name

    return render(request, 'user.html',{'owner': s_name,'sender_id':int(sender),'receiver_id':int(receiver) ,'all': all,'receiver':r_name})
@csrf_exempt
def savemess(request):
    a=Messages.objects.all()
    if request.method == 'POST':
        message = request.POST.get('description')
        senderr = request.POST.get('sender')
        sender=userlogin.objects.get(userid=int(senderr))
        receiverr = request.POST.get('receiver')
        receiver=userlogin.objects.get(userid=int(receiverr))
        b1 = Messages(description=message, sender_name=sender, receiver_name=receiver)
        b1.save()
        return JsonResponse({'status': 'save'}, safe=False)
    else:
        return JsonResponse({'status': 0}, safe=False)

def messages(request,sender,receiver):
    if request.method == 'GET':
        print('get')
        messages = Messages.objects.filter(sender_name=sender, receiver_name=receiver) | Messages.objects.filter(
            sender_name=receiver, receiver_name=sender)

        message = serializers.serialize('json', messages)

        return JsonResponse({'messages': message}, safe=False)
