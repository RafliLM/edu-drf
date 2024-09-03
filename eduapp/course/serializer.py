from rest_framework import serializers
from .models import Course, CATEGORIES

class CourseSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    title = serializers.CharField(required=True)
    category = serializers.ChoiceField(choices=CATEGORIES, required=True)
    author = serializers.CharField(required=True)
    price = serializers.IntegerField(required=True)

    class Meta:
        model = Course
        fields = ('id', 'title', 'category', 'author', 'price', 'quota')