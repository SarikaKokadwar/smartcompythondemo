from django.contrib import admin
from smartcompythondemo.models import User, Product

# admin.site.register(User)
admin.site.register(Product)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    fields = ['username', 'name', 'email']
    list_display =['id','username', 'name']
    search_fields = ['name']