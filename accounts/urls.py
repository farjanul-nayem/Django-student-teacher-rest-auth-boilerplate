from django.urls import path, include

# from .views import signup_student, signup_teacher

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/signup', include('rest_auth.registration.urls')),
]