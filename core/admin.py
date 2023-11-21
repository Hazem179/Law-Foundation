from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import *

# Register your models here.
admin.site.unregister(User)
admin.site.unregister(Group)

admin.site.site_header = 'إدارة مؤسسة الجهني'
class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('name','short_name')

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name','short_name','description','price')


class EventAdmin(admin.ModelAdmin):
    list_display = ('name','image','date','type')


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title','link','body','image')


admin.site.register(News,NewsAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(Specialization,SpecializationAdmin)
admin.site.register(Course,CourseAdmin)

