from django.contrib import admin
from django.utils.html import mark_safe
from .models import County, Girl, Image

@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    list_display = ('name', 'girls_count')
    search_fields = ('name',)
    list_per_page = 20

    def girls_count(self, obj):
        return obj.girl_set.count()
    girls_count.short_description = 'Girls Count'

@admin.register(Girl)
class GirlAdmin(admin.ModelAdmin):
    list_display = ('name', 'county', 'image_count')
    list_filter = ('county',)
    search_fields = ('name', 'county__name')
    list_per_page = 20
    readonly_fields = ('image_count',)

    def image_count(self, obj):
        return obj.image_set.count()
    image_count.short_description = 'Image Count'

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('girl', 'image_tag', 'description', 'uploaded_at')
    readonly_fields = ('image_tag', 'uploaded_at')
    list_filter = ('girl__county',)
    search_fields = ('girl__name', 'description')
    list_per_page = 20

    def image_tag(self, obj):
        return mark_safe(f'<img src="{obj.image_file.url}" style="max-width:200px;max-height:200px;" />')
    image_tag.short_description = 'Image'

