from rest_framework import serializers
from frontapp.models import Roleprofile


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roleprofile
        fields = '__all__'
