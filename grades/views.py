from .serializers import (LessonsSerializer, TeacherSerializer, GradeSerializer, StudentsSerializer)
from .models import (Teacher, Students, Grade, Lessons)

from rest_framework.viewsets import ModelViewSet

# Create your views here.
class TeacherMVS(ModelViewSet):
  queryset = Teacher.objects.all()
  serializer_class = TeacherSerializer
  
class StudentsMVS(ModelViewSet):
  queryset = Students.objects.all()
  serializer_class = StudentsSerializer
  
class GradeMVS(ModelViewSet):
  queryset = Grade.objects.all()
  serializer_class = GradeSerializer
  
class LessonsMVS(ModelViewSet):
  queryset = Lessons.objects.all()
  serializer_class = LessonsSerializer
  