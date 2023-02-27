from rest_framework import serializers
from .models import Messages, userlogin


class MessageSerializer(serializers.ModelSerializer):

    sender_name = serializers.SlugRelatedField(many=False, slug_field='userid', queryset=userlogin.objects.all())
    receiver_name = serializers.SlugRelatedField(many=False, slug_field='userid', queryset=userlogin.objects.all())

    class Meta:
        model = Messages
        fields = ['sender_name', 'receiver_name', 'description', 'time']

