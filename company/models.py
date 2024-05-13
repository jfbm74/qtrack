# company/models.py
from django.db import models
# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=255)
    nit = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=50)
    website = models.URLField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)  
    updated_by = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Branch(models.Model):
    name = models.CharField(max_length=255, verbose_name="Branch Name")
    address = models.TextField(verbose_name="Branch Address")
    email_enabled = models.BooleanField(default=False, verbose_name="Email Notifications Enabled")
    agent_count = models.IntegerField(default=0, verbose_name="Number of Agents")
    telephone = models.CharField(max_length=50, blank=True, null=True, verbose_name="Telephone Number")
    email = models.EmailField(max_length=254, blank=True, null=True, verbose_name="Email Address")
    mobile = models.CharField(max_length=50, blank=True, null=True, verbose_name="Mobile Number")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")
    updated_by = models.CharField(max_length=100, verbose_name="Updated By")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    created_by = models.CharField(max_length=100, verbose_name="Created By")
    
    def __str__(self):
        return self.name


class Module(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='modules')
    name = models.CharField(max_length=255, verbose_name="Module Name")
    description = models.TextField(verbose_name="Module Description")
    is_active = models.BooleanField(default=True, verbose_name="Active Status")

    def __str__(self):
        return f"{self.name} - {self.branch.name}"

class ServiceArea(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='service_areas', verbose_name="Branch")
    name = models.CharField(max_length=255, verbose_name="Service Name")
    description = models.TextField(verbose_name="Service Description")
    service_letter = models.CharField(max_length=1, verbose_name="Service Letter", help_text="Initial letter for service identification")
    is_active = models.BooleanField(default=True, verbose_name="Service Status")
    desks = models.IntegerField(default=1, verbose_name="Number of Desks")
    waiting_time_sla = models.IntegerField(default=0, verbose_name="Waiting Time SLA (min)", help_text="Service Level Agreement for waiting time in minutes")
    serving_time_sla = models.IntegerField(default=0, verbose_name="Serving Time SLA (min)", help_text="Service Level Agreement for serving time in minutes")
    duration = models.IntegerField(default=0, verbose_name="Service Duration (min)", help_text="Estimated duration of the service in minutes")

    def __str__(self):
        return f"{self.name} ({self.service_letter})"
