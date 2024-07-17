from django.shortcuts import render,  redirect, get_object_or_404
from .models import Ticket
from datetime import datetime
from .forms import TicketForm

def ticket_list(request):
    return render(request, 'ticket_list.html')

def registrarticket(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        asunto = request.POST['asunto']
        descripcion = request.POST['descripcion']
        departamento = request.POST['departamento']
        estado = request.POST['estado']
        fecha_str = request.POST.get('fecha')
        fecha = datetime.strptime(fecha_str, '%Y-%m-%d')

        # Nuevo campo: importancia
        importancia = request.POST.get('importancia')

        ticket = Ticket.objects.create(titulo=titulo, asunto=asunto, descripcion=descripcion,
                                       departamento=departamento, estado=estado, fecha=fecha,
                                       importancia=importancia)
        return redirect('ticket_list')
    else:
        return render(request, 'tickets/ticket_list.html')

def editarticket(request, id):
    ticket = get_object_or_404(Ticket, id=id)
    
    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            return redirect('ticket_list')
    else:
        form = TicketForm(instance=ticket)  

    return render(request, 'tickets/editar_ticket.html', {'form': form, 'ticket': ticket})

def eliminarticket(request, id):
    ticket = Ticket.objects.get(id=id)
    ticket.delete()
    return redirect('ticket_list')