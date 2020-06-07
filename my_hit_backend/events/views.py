from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Event
from .forms import EventForm

# Create your views here.
@login_required
def get_all_events(request):
    template_name = 'events/events_list.html'
    events_list = Event.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(events_list, 5)
    qs = paginator.get_page(page)
    context = {
        'obj': qs
    }
    return render(request, template_name, context)


@login_required
def delete_event(request, pk):
    qs = get_object_or_404(Event, pk=pk)
    template_name = 'events/event_delete.html'
    if request.method == 'POST':
        qs.delete()
        messages.success(request, 'event successfully deleted.')
        return redirect('events:all')
    return render(request, template_name, {'obj': qs})


@login_required
def event_details(request, pk):
    qs = get_object_or_404(Event, pk=pk)
    template_name = 'events/event_details.html'
    context = {
        'obj': qs
    }
    return render(request, template_name, context)


@login_required
def event_create(request):
    template_name = 'events/event_create.html'
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Event successfully created.')
            return redirect(reverse('events:all'))
    else:
        form = EventForm()
    return render(request, template_name, {'form': form})


@login_required
def event_update(request, pk):
    template_name = 'events/event_edit.html'
    qs = get_object_or_404(Event, pk=pk)
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES, instance=qs)
        print(form.errors.as_data())
        if form.is_valid():
            form.save()
            messages.success(request, 'Update succesfull.')
            return redirect('events:details', pk=pk)
    else:
        context = {'form': EventForm(instance=qs)}
    return render(request, template_name, context)
