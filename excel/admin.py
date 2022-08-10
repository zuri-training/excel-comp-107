from django.contrib import admin

from .models import Post, Document

# class PostAdmin(admin.ModelAdmin):
#     list_filter = ('documents', )

admin.site.register(Post)
admin.site.register(Document)

