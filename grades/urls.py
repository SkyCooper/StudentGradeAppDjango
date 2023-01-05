from django.urls import path, include
from .views import (LessonsMVS, TeacherMVS, GradeMVS, StudentsMVS)
from rest_framework import routers


router = routers.DefaultRouter()
router.register("teacher", TeacherMVS)
router.register("student", StudentsMVS)
router.register("lesson", LessonsMVS)
router.register("grade", GradeMVS)


urlpatterns =  router.urls