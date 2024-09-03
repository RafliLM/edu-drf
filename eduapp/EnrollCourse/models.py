from django.db import models
from authentication.models import CustomUser
from course.models import Course

# Create your models here.
class EnrollCourse(models.Model):
    user = models.ForeignKey(CustomUser)
    course = models.ForeignKey(Course)
    