from django.urls import path
from .views import ListCreateCourseView, RetrieveUpdateDestroyCourseView 
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', ListCreateCourseView.as_view(), name='Get and Create Courses'),
    path('<int:pk>/', RetrieveUpdateDestroyCourseView.as_view(), name="Get By Id, Update, and Delete Course")
]