from faker import Faker
from .models import (Teacher, Students, Grade, Lessons)

def run():
  fake = Faker(['tr-TR'])
  for _ in range(5):
    teacher = Teacher.objects.create(name = fake.first_name())
    lesson = Lessons.objects.create(name = fake.domain_name(), teacher=teacher)
  for _ in range(5):
    student = Students.objects.create(first_name = fake.first_name(), last_name = fake.last_name(), number = fake.pyint())
    
  print('Finished')
