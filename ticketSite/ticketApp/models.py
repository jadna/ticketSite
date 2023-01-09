from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class TicketStatus(models.TextChoices):
	TO_DO = 'To Do'
	IN_PROGRESS = 'In Progress'
	IN_REVIEW = 'In Review'
	DONE = 'Done'

class TicketType(models.TextChoices):
	SERVICE_REQUEST = 'Service Request'
	INCIDENT = 'Incident'

class AppName(models.TextChoices):
    APP1 = 'Aplication 1'
    APP2 = 'Aplication 2'
    APP3 = 'Aplication 3'
    APP4 = 'Aplication 4'

class Ticket(models.Model):
    title = models.CharField(max_length=100)
    assignee = models.ForeignKey(User, null=True, blank = True, on_delete=models.CASCADE)
    app_name = models.CharField(max_length=30, choices=AppName.choices)
    status = models.CharField(max_length=30, choices=TicketStatus.choices)
    ticket_type = models.CharField(max_length=30, choices=TicketType.choices)
    description = models.TextField()
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)

class Comments(models.Model):
    assignee = models.ForeignKey(User, null=True, blank = True, on_delete=models.CASCADE)
    ticket_id = models.ForeignKey(Ticket, null=True, blank = True, on_delete=models.CASCADE)
    comments = models.TextField()
    created_at = models.DateTimeField('created at', auto_now_add=True)
    updated_at = models.DateTimeField('updated at', auto_now=True)