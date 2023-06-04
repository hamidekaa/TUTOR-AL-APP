from rest_framework import serializers
from .models import Tutorial


class TutorialSeralizer(serializers.ModelSerializer):
     class Meta:
         model = Tutorial
         fields = '__all__'
    
     def validate(self, data):
        if data['title'] == data['description']:
            raise serializers.ValidationError({'message': 'Title and desc must not be same'})     
        return data