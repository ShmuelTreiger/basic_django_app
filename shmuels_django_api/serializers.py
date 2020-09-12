from rest_framework import serializers
from .models import Greetings


class GreetingsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Greetings
        fields = ('greeting', 'created_at',)
