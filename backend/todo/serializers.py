# creating serializers to convert model instances to JSON
from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id','title', 'description', 'completed')

