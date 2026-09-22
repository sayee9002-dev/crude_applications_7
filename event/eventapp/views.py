from django.shortcuts import render,redirect,get_object_or_404
from .models import Event
from django.contrib import messages

# Create your views here.
def event_list(request):
    events = Event.objects.all()
    return render(request, 'events/event_list.html', {'events': events})

def event_add(request):
    if request.method == 'POST':
        Event.objects.create(
            event_name=request.POST.get('event_name'),
            venue=request.POST.get('venue'),
            event_date=request.POST.get('event_date'),
            organizer=request.POST.get('organizer'),
            ticket_price=request.POST.get('ticket_price')
        )
        messages.success(request, 'Event added successfully!')
        return redirect('event_list')
    return render(request, 'events/event_add.html')

def event_edit(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.event_name=request.POST.get('event_name')
        event.venue=request.POST.get('venue')
        event.event_date=request.POST.get('event_date')
        event.organizer=request.POST.get('organizer')
        event.ticket_price=request.POST.get('ticket_price')
        
        event.save()
        messages.success(request, 'Event updated successfully!')
        return redirect('event_list')
    return render(request, 'events/event_edit.html', {'event': event})

def event_delete(request, pk):
    event = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        event.delete()
        messages.success(request, 'Event deleted successfully!')
        return redirect('event_list')
    return render(request, 'events/event_delete.html', {'event': event})
