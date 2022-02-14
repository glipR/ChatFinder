from django.urls import path, re_path
from chat_codes import views

urlpatterns = [
    re_path('^chat_codes/(?P<university>.+)/$', views.ChatCodeList.as_view()),
]