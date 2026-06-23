from django.contrib import admin
from django.contrib.auth.models import User
from .models import *
class Info_detail(admin.ModelAdmin):
    list_display = ('name','city','age')
    list_editable = ('age',)

class Opinion_detail(admin.ModelAdmin):
    list_display = ('name','job','detail')
    list_editable = ('detail',)
    list_per_page = 10
    search_fields = ['name','job','detail']
class Form_detail(admin.ModelAdmin):
    list_display = ('name','message')
    list_per_page = 10
# Register your models here.
admin.site.register(Info, Info_detail)
admin.site.register(Education)
admin.site.register(Career)
admin.site.register(Services)
admin.site.register(Customer)
admin.site.register(Opinion,Opinion_detail)
admin.site.register(Plan)
admin.site.register(Form,Form_detail)
admin.site.register(Portfolio)