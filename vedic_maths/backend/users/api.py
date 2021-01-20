from rest_framework import viewsets, permissions
from .serializers import RegistrationSerializer
from rest_framework.permissions import AllowAny
from .models import User
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout
from django.http import JsonResponse


@csrf_exempt
def signIn(request):
    if not request.method == 'POST':
        return JsonResponse({"error":"Send a Post Request with valid parameters"})
    
    username = request.POST['email']
    password = request.POST['password']
    

    try:
        user = User.objects.get(email=username)

        if user.check_password(password):
            
            login(request,user)
            serializer = RegistrationSerializer(user, many=False)
            return JsonResponse({"user":serializer.data})
        else:
            return JsonResponse({"error":"Authentication Failed Check your username and Password"})
    except User.DoesNotExist:
        return JsonResponse({"error":"Authentication Failed Check your username and Password"})



class RegisterAPI(viewsets.ModelViewSet):
    permission_classes_by_action = {"create" : {AllowAny}}

    queryset = User.objects.all().order_by('id')
    serializer_class = RegistrationSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]
