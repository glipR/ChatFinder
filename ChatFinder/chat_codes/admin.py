from django.contrib import admin
from .models import ChatCode

class ChatCodeAdmin(admin.ModelAdmin):
    pass
admin.site.register(ChatCode, ChatCodeAdmin)