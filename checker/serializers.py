from rest_framework import serializers
from .models import Data,Apidocument

class DataSerializer(serializers.ModelSerializer):
    document = serializers.FileField(max_length=None,use_url =True)
    class Meta():
        model = Apidocument
        fields = ('uploaded_at','document')
    # def create(self, validated_data):
    #     return Apidocument.objects.create(**validated_data)
