from django.contrib import admin
from .models import Post, PinPost


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['create_date', 'title',
                    'change_date']


class PinPostAdmin(admin.ModelAdmin):
    list_display = ['pin', 'create_date', 'title',
                    'change_date']


admin.site.register(Post, PostAdmin)
admin.site.register(PinPost, PinPostAdmin)
