from django.contrib import admin
from .models import Plant, Category, Tag


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class PlantCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class PlantAdmin(admin.ModelAdmin):
    pass
