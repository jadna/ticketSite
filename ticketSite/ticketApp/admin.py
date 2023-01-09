from django.contrib import admin
from .models import Ticket

class TicketAdmin(admin.ModelAdmin):
	date_hierarchy = 'created_at'
	list_filter = ('status', 'app_name', 'ticket_type', 'assignee')
	list_display = ('id', 'title', 'app_name', 'status', 'ticket_type', 'assignee', 'description', 'updated_at', 'comments')
	search_fields = ['title', 'app_name', 'status']

admin.site.register(Ticket, TicketAdmin)
