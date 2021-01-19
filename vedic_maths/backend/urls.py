from django.urls import path, include

urlpatterns = [
    path('courses/', include('backend.courses.urls'))
]
