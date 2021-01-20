from django.urls import path, include

urlpatterns = [
    path('courses/', include('backend.courses.urls')),
    path('', include('backend.users.urls')),
    path('ecommerce', include('backend.ecommerce.urls')),
]
