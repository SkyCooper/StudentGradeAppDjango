from django.db import models

# Create your models here.
class Teacher(models.Model):
  name = models.CharField(max_length=50)
  
  def __str__(self):
      return self.name
    
class Lessons(models.Model):
  name = models.CharField(max_length=50)
  teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE )
  
  def __str__(self):
      return self.name
    
class Students(models.Model):
  number = models.IntegerField()
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  
  def __str__(self):
      return self.first_name
    
class Grade(models.Model):
  student = models.ForeignKey(Students,  on_delete=models.CASCADE, related_name="student_grades")
  lesson = models.ForeignKey(Lessons,  on_delete=models.CASCADE, related_name="lesson_grades")
  grade = models.IntegerField()
  
  class Meta:
    unique_together = ('student', 'lesson')
  
  def __str__(self):
      return str(self.grade)