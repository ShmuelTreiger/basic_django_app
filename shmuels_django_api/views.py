from django.shortcuts import render_to_response
from rest_framework import viewsets

from .serializers import GreetingsSerializer
from .models import Greetings


def greetings(reuqest):
    latest_greeting = Greetings.objects.all().order_by('-created_at')[0]
    context = {
        'greetings': latest_greeting
    }
    return render_to_response('Greetings.html', context=context)


class GreetingsViewSet(viewsets.ModelViewSet):
    model = Greetings
    queryset = Greetings.objects.all().order_by('-created_at')
    serializer_class = GreetingsSerializer
