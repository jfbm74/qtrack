from django.contrib import admin

# Register your models here.
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_number', 'branch', 'company', 'service_area', 'issue_time', 'status')
    list_filter = ('status', 'branch', 'company', 'service_area')
    search_fields = ('ticket_number', 'notes')
    date_hierarchy = 'issue_time'  # Permite navegar rápidamente por fechas
    readonly_fields = ('issue_time',)  # Marca el tiempo de emisión como solo lectura

    fieldsets = (
        (None, {
            'fields': ('ticket_number', 'branch', 'company', 'service_area')
        }),
        ('Status and Notes', {
            'fields': ('status', 'notes')
        }),
        ('Date Information', {
            'fields': ('issue_time',)
        }),
    )

# Registra el modelo y el admin personalizado
admin.site.register(Ticket, TicketAdmin)
