from django.contrib import admin
from .models import Company, Branch, ServiceArea, Module, FieldConfiguration

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'nit', 'category', 'email', 'phone', 'created_at', 'updated_at')
    search_fields = ('name', 'nit', 'email')
    list_filter = ('category', 'created_at')
    ordering = ('name',)

class BranchAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'agent_count', 'telephone', 'email', 'mobile', 'created_at', 'updated_at']
    search_fields = ['name', 'address']
    list_filter = ['email_enabled', 'created_at']
    
class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'branch', 'description', 'is_active']
    list_filter = ['is_active', 'branch']
    search_fields = ['name', 'description']

class ServiceAreaAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_letter', 'branch', 'is_active', 'desks', 'waiting_time_sla', 'serving_time_sla', 'duration')
    list_filter = ('is_active', 'service_letter', 'branch')
    search_fields = ('name', 'description')

class FieldConfigurationAdmin(admin.ModelAdmin):
    list_display = ('field_name', 'service_area', 'field_type', 'required', 'description')
    list_filter = ('field_type', 'required', 'service_area')
    search_fields = ('field_name', 'description')

admin.site.register(Company, CompanyAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(ServiceArea, ServiceAreaAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(FieldConfiguration, FieldConfigurationAdmin)
