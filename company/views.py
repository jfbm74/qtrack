from django.shortcuts import render, redirect, get_object_or_404
from .models import Company, Branch, ServiceArea
from django.urls import reverse
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from .forms import BranchForm, ServiceAreaForm
from django.views import View



def company_list(request):
    companies = Company.objects.all()
    return render(request, 'config/company/companies-index.html', {'companies': companies})

@require_http_methods(["POST"])
def add_company(request):
    if request.method == 'POST':
        # Extrae datos del formulario
        name = request.POST.get('name')
        nit = request.POST.get('nit')
        category = request.POST.get('category')
        address = request.POST.get('address', '')
        phone = request.POST.get('phone', '')
        email = request.POST.get('email')
        website = request.POST.get('website', '')

        # Manejar carga de archivo si hay un campo para el logo
        #logo = request.FILES.get('logo', None)

        # Crea y guarda la nueva compañía
        company = Company(
            name=name,
            nit=nit,
            category=category,
            address=address,
            phone=phone,
            email=email,
            website=website,
            #logo=logo  # Asegúrate de que tu modelo soporte un campo de imagen para logo
        )
        company.save()

        # Mensaje de éxito
        messages.success(request, 'Company added successfully.')
        return redirect(reverse('company-list'))  # Redirecciona a donde quieras después de guardar

    # Si no es POST, simplemente renderiza el formulario (o puedes redireccionar a otra parte)
    return render(request, 'company-list')


def delete_company(request, company_id):
    if request.method == 'POST':  # Asegúrate de que la eliminación se haga mediante una solicitud POST
        company = get_object_or_404(Company, pk=company_id)
        company.delete()
        messages.success(request, 'Company deleted successfully.')
        return redirect('company-list')  # Usa el nombre correcto de la URL aquí
    else:
        messages.error(request, "Invalid method")
        return redirect('company-list')  # Asegúrate de redirigir a una URL existente aquí también
    
def update_company(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    if request.method == 'POST':
        # Actualiza los datos de la empresa
        company.name = request.POST.get('name', company.name)
        company.nit = request.POST.get('nit', company.nit)
        company.category = request.POST.get('category', company.category)
        company.address = request.POST.get('address', company.address)
        company.phone = request.POST.get('phone', company.phone)
        company.email = request.POST.get('email', company.email)
        company.website = request.POST.get('website', company.website)
        # company.logo = request.FILES.get('logo', company.logo)  # Descomentar si el modelo maneja logos

        company.save()
        messages.success(request, 'Company updated successfully.')
        return redirect('company-list')
    else:
        # Carga el formulario con los datos existentes
        return render(request, 'config/company/update-company.html', {'company': company})


def list_branches(request):
    branches = Branch.objects.all()  # Retrieves all branches from the database
    services = ServiceArea.objects.all()  # Retrieves all services from the database
    print(services)
    return render(request, 'config/company/branch-index.html', {'branches': branches, 'services': services})


class AddBranchView(View):
    form_class = BranchForm
    
    def get(self, request):
        form = self.form_class()        
        return render(request, 'config/users/add_branch.html', {'form': form})
       
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            new_branch = form.save()
            messages.success(request, 'Sede agregada con éxito.')
            return redirect('list-branches') 
        else:
            messages.error(request, 'Por favor corrija los errores en el formulario.')
            print("form errors:", form.errors)           
            print(messages.error)
            # return render(request, self.template_name, {'form': form})
            branches = Branch.objects.all()  # Retrieves all branches from the database
            return render(request, 'config/company/branch-index.html', {'branches': branches})


def list_services(request):
    services = ServiceArea.objects.all()  # Retrieves all services from the database
    branches = Branch.objects.all()  # Retrieves all branches from the database
    return render(request, 'config/services/services-index.html', {'services': services, 'branches': branches})


def add_servicearea(request):
    if request.method == 'POST':
        form = ServiceAreaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-services')  # Redirect to the list of service areas or another appropriate page
    else:
        form = ServiceAreaForm()
    return render(request, 'config/services/services-index.html', {'form': form})