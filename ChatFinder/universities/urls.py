from django.urls import path
from universities import views

urlpatterns = [
    path('universities/', views.UniversityList.as_view()),
]