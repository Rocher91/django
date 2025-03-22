from django.contrib import admin

from OrderManagement.models import Clients,Items,Orders

# Register your models here.

class ClientsAdmin( admin.ModelAdmin ):
    list_display = ("name","address","phone")
    search_fields = ("name","phone")

class ItemsAdmin( admin.ModelAdmin):
    list_filter = ("section",)

class OrderAdmin( admin.ModelAdmin ):
    list_display= ("num","date")
    list_filter = ("date",)
    date_hierarchy = "date"

admin.site.register( Clients, ClientsAdmin )
admin.site.register( Items, ItemsAdmin )
admin.site.register( Orders,OrderAdmin )