from django.db import models
class Course(models.Model):
    CourseID=models.IntegerField(primary_key=True)
    CourseName=models.CharField(max_length=100)
    Credits=models.FloatField()
   
    

    
