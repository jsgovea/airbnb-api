from rest_framework import serializers

from users.serializers import UserSerializer
from .models import Room


class RoomSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Room
        fields = '__all__'


class WriteRoomSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=140)
    address = serializers.CharField(max_length=140)
    price = serializers.IntegerField(help_text="USD per night")
    beds = serializers.IntegerField(default=1)
    lat = serializers.DecimalField(max_digits=10, decimal_places=6)
    lng = serializers.DecimalField(max_digits=10, decimal_places=6)
    bedrooms = serializers.IntegerField(default=1)
    bathrooms = serializers.IntegerField(default=1)
    check_in = serializers.TimeField(default="00:00:00")
    check_out = serializers.TimeField(default="00:00:00")
    instant_book = serializers.BooleanField(default=False)

    def create(self, validated_data):
        return Room.objects.create(**validated_data)

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

    def update(self, instance, validated_data):
        instance.name = validated_data('name', instance.name)
        instance.address = validated_data('address', instance.address)
        instance.price = validated_data('price', instance.price)
        instance.beds = validated_data('beds', instance.beds)
        instance.lat = validated_data('lat', instance.lat)
        instance.lng = validated_data('lng', instance.lng)
        instance.bedrooms = validated_data('bedrooms', instance.bedrooms)
        instance.bathrooms = validated_data('bathrooms', instance.bathrooms)
        instance.check_in = validated_data('check_in', instance.check_in)
        instance.check_out = validated_data('check_out', instance.check_out)
        instance.instant_book = validated_data('instant_book', instance.instant_book)

        instance.save()
        return instance
