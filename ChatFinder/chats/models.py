from django.db import models
from chat_codes.models import ChatCode

class Chat(models.Model):

    GROUP_CHOICES = (
        ("discord", "Discord"),
        ("facebook", "Facebook"),
        ("other", "Other"),
    )

    chat_code = models.ForeignKey(ChatCode, on_delete=models.CASCADE)
    group_type = models.CharField(max_length=255, choices=GROUP_CHOICES)
    show_name = models.CharField(max_length=255)
    year = models.IntegerField()

    id = models.AutoField(primary_key=True)

    def __str__(self) -> str:
        return self.show_name
