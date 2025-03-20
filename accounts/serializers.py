from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    confirm_password = serializers.CharField(write_only=True, required=True)
    profile_image = serializers.ImageField(required=False)  # Allow profile image upload (optional)

    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'email', 'password', 'confirm_password', 'profile_image')

    def validate(self, attrs):
        if attrs['password'] != attrs['confirm_password']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return attrs

    def create(self, validated_data):
        # Remove confirm_password from data
        validated_data.pop('confirm_password')
        # Extract profile_image if provided
        profile_image = validated_data.pop('profile_image', None)

        # Create the user instance
        user = CustomUser.objects.create(
            email=validated_data['email'],
            name=validated_data.get('name', '')
        )
        if profile_image:
            user.profile_image = profile_image

        user.set_password(validated_data['password'])
        user.save()
        return user

class UserProfileSerializer(serializers.ModelSerializer):
    profile_image_url = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ('id', 'name', 'email', 'profile_image', 'profile_image_url')
        extra_kwargs = {
            'profile_image': {'required': False},  # Allow updates without requiring an image
        }

    def get_profile_image_url(self, obj):
        request = self.context.get('request')
        if obj.profile_image:
            image_url = obj.profile_image.url
            return request.build_absolute_uri(image_url) if request else image_url
        return None
