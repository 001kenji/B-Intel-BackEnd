from django.shortcuts import render,HttpResponse,loader
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse

from .models import User
from .sterializer import UserSterializer
# Create your views here.

@api_view(['GET'])
def viewDB(request):
    userDB = User.objects.all().values()
    DBserializer = UserSterializer(userDB, many=True)
    return Response(DBserializer.data)

@api_view(['GET', 'POST', 'PUT'])
def Commit(request):
 
    if request.method == 'POST':
        print('called in POST method')
        data = json.loads(request.body.decode("utf-8"))
        #print('data is', data)
        #print(data)
        mydata = User.objects.filter(name=data['name'],pass_code=data['password']).values()
        
        datadisp = UserSterializer(mydata, many=True)
        print(datadisp.data)
        if mydata :
            content = {
                'found' : True,
                'profile' : datadisp.data,
                'position': mydata[0]['id']
            }
            
            return JsonResponse(json.dumps(content), safe=False)
            
        content = {
                'found' : False
            }
        return JsonResponse(json.dumps(content), safe=False)

    if request.method == 'PUT':
        print('called in PUT method')
        data = json.loads(request.body.decode("utf-8"))
        #print(data)
        mydata = User.objects.filter(name=data['name'],pass_code=data['password']).values()
        
        if len(mydata) > 0 :
            print(len(mydata))
            content = {
                'exists' : True,
            }
            return JsonResponse(json.dumps(content), safe=False)
        
        elif len(mydata) == 0:
            newUser = User(name= data['name'],pass_code= data['password'], email = data['email'])
            newUser.save()
            print('written')
            content = {
                'exists': False,
                'response' : 'success'
            }
            return JsonResponse(json.dumps(content), safe=False)


def DashBoard(request):
    homepage = loader.get_template('home.html')
    return HttpResponse(homepage.render())

def Test(request):
    homepage = loader.get_template('index.html')
    return HttpResponse(homepage.render())
