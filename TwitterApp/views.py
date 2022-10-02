from rest_framework.parsers import JSONParser
from rest_framework.views import APIView  
from rest_framework.response import Response  
from rest_framework import status

from TwitterApp.models import Users,Tweets
from TwitterApp.serializers import UsersSerializer,TweetsSerializer

# Create your views here.
class UsersView(APIView):
    
    def get(self,request):
        users=Users.objects.all()
        users_serializer=UsersSerializer(users,many=True)
        return Response({'status': 'success', "users":users_serializer.data}, status=200) 

    def post(self, request):
        users_data=JSONParser().parse(request)
        users_serializer=UsersSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return Response({"status": "success", "data": users_serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": users_serializer.errors}, status=status.HTTP_400_BAD_REQUEST) 

class TweetsView(APIView):
    
    def get(self,request):
        tweets=Tweets.objects.all()
        tweets_serializer=TweetsSerializer(tweets,many=True)
        return Response({'status': 'success', "tweets":tweets_serializer.data}, status=200) 

    def post(self, request):
        tweets_data=JSONParser().parse(request)
        tweets_serializer=TweetsSerializer(data=tweets_data)
        if tweets_serializer.is_valid():
            tweets_serializer.save()
            return Response({"status": "success", "data": tweets_serializer.data}, status=status.HTTP_200_OK)  
        else:  
            return Response({"status": "error", "data": tweets_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)