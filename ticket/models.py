
# Create your models here.
from django.db import models
from django.utils import timezone
from company.models import Branch, Company, ServiceArea
from django.db.models import Max  # Import Max for aggregation


class Ticket(models.Model):
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    service_area = models.ForeignKey(ServiceArea, on_delete=models.CASCADE)
    ticket_number = models.CharField(max_length=20, unique=True, blank=True)
    issue_time = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, default='waiting', choices=(
        ('waiting', 'Waiting'),
        ('serving', 'Serving'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ))
    notes = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.ticket_number:
            today = timezone.localdate()
            # Filter tickets from the same day and service area
            last_ticket = Ticket.objects.filter(
                issue_time__date=today,
                service_area=self.service_area
            ).aggregate(Max('ticket_number'))
            last_number = 0
            if last_ticket['ticket_number__max']:
                # Extracts the numeric part and increments it by one
                last_number = int(last_ticket['ticket_number__max'].split('-')[-1])
            # Generate new ticket number
            self.ticket_number = f"{self.service_area.service_letter}-{last_number + 1:03d}"
        super(Ticket, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.ticket_number} - {self.status}"
