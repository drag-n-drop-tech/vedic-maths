from django.urls import path, include
from rest_framework import routers

from .api import (
    CoursesViewset, Course_cat_viewset, CourseInstractorViewSet
)
router = routers.DefaultRouter()

router.register('courses', CoursesViewset, 'courses')
router.register('courseCategory', Course_cat_viewset, 'courses')
router.register('courseInstractor', CourseInstractorViewSet, 'courses')

urlpatterns = [
    path('', include(router.urls))
]
