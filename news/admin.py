from django.utils.html import format_html
from django.contrib import admin
from .models import News

admin.site.site_header = "News Website Admin"
admin.site.site_title = "News Management"
admin.site.index_title = "Welcome to the News Admin Panel"

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'image_preview') 

    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: auto;" />', obj.image)
        return "No Image"

    image_preview.short_description = "Image Preview"
