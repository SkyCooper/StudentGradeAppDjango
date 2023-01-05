from rest_framework import serializers
from .models import (Teacher, Students, Grade, Lessons)

class GradeSerializer(serializers.ModelSerializer):
  student = serializers.StringRelatedField()
  lesson = serializers.StringRelatedField()
  class Meta:
    model = Grade
    fields = ("student", "lesson", "grade")
    
  

class TeacherSerializer(serializers.ModelSerializer):
  class Meta:
    model = Teacher
    fields = ("id", "name")
    
    
class LessonsSerializer(serializers.ModelSerializer):
  lesson_grades = GradeSerializer(many=True)
  class Meta:
    model = Lessons
    fields = ("id", "name", "teacher", "lesson_grades")
    
    
class StudentsSerializer(serializers.ModelSerializer):
  student_grades = GradeSerializer(many=True)
  class Meta:
    model = Students
    fields = ("number", "first_name", "last_name", "student_grades")
    
    
