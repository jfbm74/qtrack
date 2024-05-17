from django.urls import path
from .views import create_ticket, select_service_view, ticket_detail_view

urlpatterns = [
    path('ticket-create/', select_service_view, name='ticket-create'),
    path('create-ticket/<int:service_id>/', create_ticket, name='create_ticket'),  # Ensure the correct URL name
    path('ticket-detail/<int:ticket_id>/', ticket_detail_view, name='ticket-detail'),
]