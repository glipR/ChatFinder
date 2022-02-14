from .models import Chat
from .serializers import ChatSerializer
from rest_framework import generics


class ChatList(generics.ListCreateAPIView):
    serializer_class = ChatSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        chat_code = self.kwargs['chat_code']
        return Chat.objects.filter(chat_code=chat_code)
