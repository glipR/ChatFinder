from django.db import models
from universities.models import University

class ChatCode(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    show_name = models.CharField(max_length=255)

    id = models.AutoField(primary_key=True)

    def __str__(self) -> str:
        return self.show_name