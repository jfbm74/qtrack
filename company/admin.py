from django.contrib import admin
from .models import Company, Branch, ServiceArea

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'nit', 'category', 'email', 'phone', 'created_at', 'updated_at')
    search_fields = ('name', 'nit', 'email')
    list_filter = ('category', 'created_at')
    ordering = ('name',)

class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'agent_count', 'telephone', 'email', 'mobile']

    
class ServiceAreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_letter', 'is_active', 'desks', 'waiting_time_sla', 'serving_time_sla', 'duration')
    list_filter = ('is_active', 'service_letter')
    search_fields = ('name', 'description')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(ServiceArea, ServiceAreaAdmin)