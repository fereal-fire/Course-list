from django.db import models

# Create your models here.
class Course(models.Model):
    course_title = models.CharField(max_length=60)
    course_description = models.CharField(max_length= 128)
    credits = models.PositiveSmallIntegerField()
    instructor = models.CharField(max_length=64)
    start_date = models.DateField()

    def __str__(self):
        return self.course_title