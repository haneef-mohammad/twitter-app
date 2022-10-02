from rest_framework import serializers
from TwitterApp.models import Users,Tweets

class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=Users
        fields=('UserId','UserName','Follwers','CreatedOn')

class TweetsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tweets
        fields=('TweetId','Tweet','PostedBy','PostedOn')
