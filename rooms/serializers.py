from rest_framework import serializers

from users.serializers import RelatedUserSerializer
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    user = RelatedUserSerializer()

    class Meta:
        model = Room
        fields = '__all__'


class WriteRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        exclude = ('user', 'modified', 'create')

    def validate(self, data):
        if not self.instance:
            check_in = data.get('check_in', self.instance.check_in)
            check_out = data.get('check_out', self.instance.check_out)
        else:
            check_in = data.get('check_in')
            check_out = data.get('check_out')
            if check_in == check_out:
                raise serializers.ValidationError('Not enough time between changes')
        return data
