import json
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Count, F
from django.urls import reverse
from .models import ServiceArea, Branch, Ticket
from company.forms import BranchSelectForm
from company.models import Company
from django.http import HttpResponse
from django.contrib import messages
from urllib.parse import urlencode



def select_service_view(request):
    branches = Branch.objects.all()
    if 'ticket_created' in request.session:
        del request.session['ticket_created']
        
    if request.method == 'POST':
        form = BranchSelectForm(request.POST)
        if form.is_valid():
            selected_branch = form.cleaned_data['branch']
            services = ServiceArea.objects.filter(branch=selected_branch)
        else:
            services = ServiceArea.objects.none()
        return render(request, 'tickets/create-ticket.html', {'form': form, 'services': services, 'branches': branches})
    else:
        selected_branch_id = request.session.get('selected_branch_id')
        services, form = None, None
        if selected_branch_id:
            selected_branch = Branch.objects.get(id=selected_branch_id)
            services = ServiceArea.objects.filter(branch=selected_branch)
            form = BranchSelectForm(initial={'branch': selected_branch})
        return render(request, 'tickets/create-ticket.html', {'form': form, 'services': services, 'branches': branches})
    

def create_ticket(request, service_id):
    try:
        service = get_object_or_404(ServiceArea, id=service_id)
        branch = service.branch
        company = Company.objects.get(id=16)  # Assuming company ID

        if request.method == 'POST':
            # Calculate current waiting tickets
            current_waiting_tickets = Ticket.objects.filter(
                branch=branch,
                status='waiting'
            ).count()

            # Assuming each ticket takes an average of 10 minutes
            estimated_waiting_time = (current_waiting_tickets + 1) * 10

            new_ticket = Ticket.objects.create(
                branch=branch,
                company=company,
                service_area=service,
                status='waiting'
            )

            # Construct ticket details for display
            ticket_details = {
                'number': new_ticket.ticket_number,
                'service': service.name,
                'branch': branch.name,
                'waiting_time': estimated_waiting_time,
                'waiting_count': current_waiting_tickets + 1
            }

            # Use 'render' to pass context directly to the template
            context = {
                'ticket_details': ticket_details,
                'show_modal': True  # Control flag to show modal
            }
            return render(request, 'tickets/create-ticket.html', context)
        else:
            return HttpResponse("Method not allowed", status=405)
    except Exception as e:
        messages.error(request, f'Error creating ticket: {str(e)}')
        return redirect('ticket-create')



def ticket_detail_view(request, ticket_id):
    ticket = get_object_or_404(Ticket, id=ticket_id)
    context = {
        'ticket': ticket,
        'service': ticket.service_area,
        'branch': ticket.branch
    }
    return render(request, 'ticket_detail.html', context)