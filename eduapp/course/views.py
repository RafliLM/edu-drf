from rest_framework import generics
from rest_framework.permissions import AllowAny
from .serializer import CourseSerializer
from .models import Course

# Create your views here.
class ListCreateCourseView(generics.ListCreateAPIView):
    serializer_class=CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.all()
        category = self.request.query_params.get('category')
        if category is not None:
            queryset = queryset.filter(category=category)
        return queryset

class RetrieveUpdateDestroyCourseView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class=CourseSerializer
    