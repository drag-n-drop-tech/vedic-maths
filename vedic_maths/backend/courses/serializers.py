from rest_framework import serializers

from .models import CourseInstructors, CourseCategories, Courses

class CoursesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'


class CourseCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseCategories
        fields = '__all__'



class CourseInstructorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseInstructors
        fields = '__all__'