from rest_framework import serializers 
from apps.main_models.user_models import User 

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username", 
            "first_name", 
            "last_name", 
            "email", 
            "phone_number", 
            "national_code",
            "gender", 
            "birth_date", 
            "user_type",
            "is_staff",
            "is_active",
            "profile_image"
        ]
        extra_kwargs = {
            "password": {"write_only":True}, 
            "email": {"reqired":True}
        }

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
    
    def validate_phone_number(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("Phone number must contain only digits.")
        if len(value) != 11:
            raise serializers.ValidationError("Phone number must be exactly 11 digits.")
        return value
    
    def validate_national_code(self, value):
        if not value.isdigit():
            raise serializers.ValidationError("National code must contain only digits.")
        if len(value) != 10:
            raise serializers.ValidationError("National code must be exactly 10 digits.") 
        return value 
