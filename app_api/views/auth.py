from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from app_api.models.user import MyOpsUser


@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    '''Handles the authentication of a user

    Method arguments:
      request -- The full HTTP request object
    '''
    username = request.data['username']
    password = request.data['password']

    authenticated_user = authenticate(username=username, password=password)

    if authenticated_user is not None:
        token = Token.objects.get(user=authenticated_user)
        # TODO: If you need to return more information to the client, update the data dict
        data = {
            'valid': True,
            'token': token.key
        }
    else:
        data = { 'valid': False }
    return Response(data)

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    '''Handles the creation of a new gamer for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # TODO: this is only adding the username and password, if you want to add in more user fields like first and last name update this code
    new_user = User.objects.create_user(
        username=request.data['username'],
        password=request.data['password'],
    )

    # TODO: If you're using a model with a 1 to 1 relationship to the django user, create that object here
    myops_user = MyOpsUser.objects.create(
        bio=request.data['bio'],
        username=request.data['username'],
        first_name=request.data['first_name'],
        last_name=request.data['last_name'],
        user=new_user
    )
    
    token = Token.objects.create(user=new_user)
    # TODO: If you need to send the client more information update the data dict
    
    data = { 'token': token.key }
    return Response(data, status=status.HTTP_201_CREATED)
