from django.contrib import admin

from .models import event, photo

# Register your models here.

class photoAdmin(admin.StackedInline):
    model=photo

@admin.register(event)
class eventAdmin(admin.ModelAdmin):
    inlines  = [photoAdmin]

    class Meta:
        model = event

@admin.register(photo)
class photoAdmin(admin.ModelAdmin):
    pass