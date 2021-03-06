from django.contrib import admin
from .models import Volunteer, Animal, ContactModel


class VolunteerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "friendly_name",
        "about",
        "image",
    )


class AnimalAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
        'type',
        'breed',
        'about',
        "image",
        "id",
    )


class ContactModelAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'email',
        'question',
    )


admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Animal, AnimalAdmin)
admin.site.register(ContactModel, ContactModelAdmin)
