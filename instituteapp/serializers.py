from rest_framework import serializers
from.models import *
class studentsdetailsserializer(serializers.ModelSerializer):
    class Meta:
        model=students_details
        fields="__all__"