from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['titulo', 'asunto', 'descripcion', 'departamento', 'estado', 'fecha', 'importancia']
        widgets = {'importancia': forms.RadioSelect(choices=Ticket.IMPORTANCIA_CHOICES),}