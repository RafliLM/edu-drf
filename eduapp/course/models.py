from django.db import models

CATEGORIES = [
    ('informasi-teknologi', 'Informasi Teknologi'),
    ('marketing', 'Marketing'),
    ('bisnis', 'Bisnis')
]

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORIES, max_length=30)
    author=models.CharField(max_length=50)
    price=models.PositiveIntegerField()
    quota=models.PositiveIntegerField(null=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.name 
