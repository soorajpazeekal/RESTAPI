from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from core.models import Luggage, Order
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import LuggageSerializer, OrderSerializer
from rest_framework.permissions import IsAuthenticated



class UsercreationView(APIView):
    def post(self, request):
        db = request.data 
        username,password = (db['username'], db['password'])
        if 'staff' in db:
            user = User.objects.create_user(username=username,  email=None, password=password, is_staff=True)
            user.save()
            return Response(data='account created. please generate access token on /api/token-auth/ endpoint', status=status.HTTP_200_OK)
        user = User.objects.create_user(username=username, email=None, password=password)   
        user.save() 
        return Response(data='account created. please generate access token on /api/token-auth/ endpoint', status=status.HTTP_200_OK)


class indexView(APIView):
    def get(self, request):
        permission_classes = (IsAuthenticated,)
        if request.user.is_authenticated: 
            return Response('please generate access token from /api/token-auth/ endpoint')
        return Response('create an account or register')


class LoginView(APIView):
    def post(self, request):
        try:
            db = request.data 
            username,password = (db['username'], db['password'])
            user = authenticate(username=username, password=password)
            if user is not None:
                return Response(data='authentication is sucessful', status=status.HTTP_200_OK)
            return Response(data='Not found any accounts', status=status.HTTP_404_NOT_FOUND) 
        except:
            return Response(data='please login', status=status.HTTP_404_NOT_FOUND)


class EditluggageView(APIView):
    def post(self, request):
        permission_classes = (IsAuthenticated,)
        username = request.user.username
        if request.user.is_staff:
            db = request.data
            created = db['created']
            try:
                testanser = Luggage.objects.get(created = username)
            except:
                if username == created:
                    luggage_types = db['Luggage_types']
                    status = db['status']
                    max_items = db['max_items']
                    data = Luggage.objects.create(created=created, luggage_types=luggage_types, status=status, max_items=max_items)
                    data.save()
                    return Response(data='recored created.')
            return Response(data='your username and created values are not matching. or you are already added a post')    
        return Response(data='you are not staff')            


    def get(self, request):
        permission_classes = (IsAuthenticated,)
        if request.user.is_staff:
            username = request.user.username
            user_objects = Luggage.objects.filter(created = username)
            serializer = LuggageSerializer(user_objects, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data='you are not staff')    



    def put(self, request):
        permission_classes = (IsAuthenticated,)
        username = request.user.username
        db = request.data 
        status = db['status']
        user_objects = Luggage.objects.get(created = username)
        data = Luggage.objects.update(status=status)
        return Response(data='ok')


class OrderView(APIView):
    def get(self, request):
        permission_classes = (IsAuthenticated,)
        username = request.user.username
        user_objects = Luggage.objects.all()
        serializer = LuggageSerializer(user_objects, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)




    def post(self, request):
        permission_classes = (IsAuthenticated,)
        db = request.data
        username = request.user.username
        luggage_types = db['Luggage_types']
        multipler = '0'
        for item in luggage_types:
            values = luggage_types[item]
            multipler = int(values)+int(multipler)
        data = Order.objects.create(user=username, luggage_types=luggage_types, amount=multipler)
        data.save()
        return Response(data='OK')





class StafforderView(APIView):
    def get(self, request):
        permission_classes = (IsAuthenticated,)
        if request.user.is_staff:
            user_objects = Order.objects.all()
            serializer = OrderSerializer(user_objects, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        username = request.user.username
        user_objects = Order.objects.filter(user = username)
        serializer = OrderSerializer(user_objects, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
