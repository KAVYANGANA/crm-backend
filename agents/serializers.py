from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Agent

User = get_user_model()


class AgentSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = Agent
        fields = [
            'id',
            'full_name',
            'phone_number',
            'whatsapp_number',
            'is_active',
            'email',
            'password',
            'confirm_password',
            'created_at',
        ]
        read_only_fields = ['id', 'created_at']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({
                "password": "Passwords do not match"
            })

        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({
                "email": "Email already exists"
            })

        return data

    def create(self, validated_data):
        email = validated_data.pop('email')
        password = validated_data.pop('password')
        validated_data.pop('confirm_password')

        # Create agent login account
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        # Create agent profile
        agent = Agent.objects.create(
            user=user,
            **validated_data
        )

        return agent