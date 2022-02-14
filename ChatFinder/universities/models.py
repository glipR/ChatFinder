from django.db import models

class University(models.Model):
    show_name = models.CharField(max_length=255)

    id = models.AutoField(primary_key=True)

    def __str__(self) -> str:
        return self.show_name
