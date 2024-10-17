from rest_framework import serializers

from notes.models import User,Task


class UserSerializer(serializers.ModelSerializer):

    password1=serializers.CharField(write_only=True)

    password2=serializers.CharField(write_only=True)

    password=serializers.CharField(read_only=True)





    class Meta:

        model=User

        fields=["id","username","email","phone","password1","password2","password"]

    def create(self,validated_data):

        password1=validated_data.pop("password1")

        password2=validated_data.pop("password2")

        return User.objects.create_user(**validated_data,password=password1)
    
    def validate(self,data):

        if data["password1"] != data["password2"]:

            raise serializers.ValidationError("Password Mismatch")
        
        return data
    
    
    

class TaskSerializer(serializers.ModelSerializer):

    owner=serializers.StringRelatedField(read_only=True)

    class Meta:

        model=Task

        fields="__all__"

        read_only_fields=[
            "id",
            "created_date",
            "owner",
            "is_active"
        ]

