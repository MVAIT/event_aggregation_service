from rest_framework import serializers
from .models import Events


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Events
        fields = ('title', 'text', 'author', 'created_date')