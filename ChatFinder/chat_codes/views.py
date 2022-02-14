from .models import ChatCode
from .serializers import ChatCodeSerializer
from rest_framework import generics


class ChatCodeList(generics.ListCreateAPIView):
    serializer_class = ChatCodeSerializer

    def get_queryset(self):
        """
        This view should return a list of all the purchases for
        the user as determined by the username portion of the URL.
        """
        university = self.kwargs['university']
        return ChatCode.objects.filter(university=university)
