from django.urls import path, re_path
from chats import views

urlpatterns = [
    re_path('^chats/(?P<chat_code>.+)/$', views.ChatList.as_view()),
]