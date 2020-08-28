from rest_framework import serializers
from .models import Events


class EventSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = ('title', 'start_date', 'end_date', 'text', 'author', 'created_date', 'location')