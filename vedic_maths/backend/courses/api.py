from rest_framework import viewsets
from rest_framework import permissions
from .models import Courses, CourseCategories, CourseInstructors


from .serializers import CoursesSerializer, CourseCategoriesSerializer, CourseInstructorsSerializer

class CoursesViewset(viewsets.ModelViewSet):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
    permissions = [
        permissions.AllowAny
    ]

class Course_cat_viewset(viewsets.ModelViewSet):
    queryset = CourseCategories.objects.all()
    serializer_class = CourseCategoriesSerializer
    permissions = [
        permissions.AllowAny
    ]
    



class CourseInstractorViewSet(viewsets.ModelViewSet):
    queryset = CourseInstructors.objects.all()
    serializer_class = CourseInstructorsSerializer
    permissions = [
        permissions.AllowAny
    ]

    