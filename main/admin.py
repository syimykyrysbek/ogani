from django.contrib import admin
from main.models import Category2, Product, OrderData, Order, Contact, Contact2

class Category2Admin(admin.ModelAdmin):
    list_display = ['name']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'description', 'image']

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'sent_at']

class Contact2Admin(admin.ModelAdmin):
    list_display = ['email', 'sent_at']

admin.site.register(Category2)
admin.site.register(Product)
admin.site.register(OrderData)
admin.site.register(Order)
admin.site.register(Contact)
admin.site.register(Contact2)


