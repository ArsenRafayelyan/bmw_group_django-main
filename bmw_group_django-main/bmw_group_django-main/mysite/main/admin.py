from django.contrib import admin
from .models import HomeVideo, Subtitle, HomeName, Content, About, Contact
# Register your models here.
admin.site.register(HomeName)
admin.site.register(HomeVideo)
admin.site.register(Subtitle)
admin.site.register(Content)
admin.site.register(About)
admin.site.register(Contact)
