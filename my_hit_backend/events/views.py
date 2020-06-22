from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from cloud_messaging.models import CloudMessaging
from pyfcm import FCMNotification
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
    push_service = FCMNotification(
        api_key="AAAAKq2O4e8:APA91bHjUnM7TTTqsb5F1xMz-H35oyjBTvaBQGRY5nYO58EVFEFmA0Z2yOlZSyIsfpAXBlsrRDNQwTUDNWKPGD2lquvDHijWOCXAtKlN7w2C-lf8smBZsy5saW7oejtT8u5sZvlLZU8-")
    name = request.POST.get('name')
    description = request.POST.get('description')
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            try:
                qs_receipiants = CloudMessaging.objects.all()
                registration_ids = []
                for e in qs_receipiants:
                    registration_ids.append(e.fcm_token)
                # Send to multiple devices by passing a list of ids.
                # registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]
                message_title = name
                message_body = description
                result = push_service.notify_multiple_devices(
                    registration_ids=registration_ids, message_title=message_title, message_body=message_body)
                print('result')
                print(result)
            except Exception as e:
                print(e)
            messages.success(request, 'Event successfully created. ')
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
