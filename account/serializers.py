from rest_framework import serializers

from account.models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)
    password_confirm = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ("email", "password", "password_confirm")

    def validate(self, validated_data):
        password = validated_data.get("password")
        password_confirm = validated_data.pop("password_confirm")
        if password != password_confirm:
            raise serializers.ValidationError("Пароли не подходят")
        return validated_data

    def create(self, validated_data):
        email = validated_data.get("email")
        password = validated_data.get("password")
        user = User.objects.create_user(email=email, password=password)
        return user
