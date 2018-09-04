from django.contrib import admin
from .models import Post, PinPost


# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_date',
                    'change_date']
    list_editable = ['title', 'create_date']


class PinPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'create_date',
                    'pin', 'change_date']
    list_editable = ['title', 'create_date']


admin.site.register(Post, PostAdmin)
admin.site.register(PinPost, PinPostAdmin)
