from django.contrib import admin

from .models import Profile,Project,Review

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user','prof_pic','bio','contact')

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Project)
admin.site.register(Review)
