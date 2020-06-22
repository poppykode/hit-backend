from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib import messages
from pyfcm import FCMNotification
from django.contrib.auth.decorators import login_required
from .forms import TimetabeForm
from .models import Timetable
from cloud_messaging.models import CloudMessaging

# Create your views here.
@login_required
def all_timetables(request):
    template_name = 'timetable/timetable_list.html'
    qs = Timetable.objects.all
    context = {
        'obj': qs
    }
    return render(request, template_name, context)


@login_required
def upload_time(request):
    template_name = 'timetable/timetable_upload.html'
    push_service = FCMNotification(
        api_key="AAAAKq2O4e8:APA91bHjUnM7TTTqsb5F1xMz-H35oyjBTvaBQGRY5nYO58EVFEFmA0Z2yOlZSyIsfpAXBlsrRDNQwTUDNWKPGD2lquvDHijWOCXAtKlN7w2C-lf8smBZsy5saW7oejtT8u5sZvlLZU8-")
    if request.method == 'POST':
        course = request.POST.get('course')
        form = TimetabeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            try:
                qs_receipiants = CloudMessaging.objects.all()
                registration_ids = []
                for e in qs_receipiants:
                    registration_ids.append(e.fcm_token)
                # Send to multiple devices by passing a list of ids.
                # registration_ids = ["<device registration_id 1>", "<device registration_id 2>", ...]
                message_title = 'Time Uploaded'
                message_body = 'Timetable for ' + course
                result = push_service.notify_multiple_devices(
                    registration_ids=registration_ids, message_title=message_title, message_body=message_body)
                print('result')
                print(result)
            except Exception as e:
                print(e)
            messages.success(request, 'Timetable successfully uploaded.')
            return redirect(reverse('timetable:all'))
    else:
        form = TimetabeForm()
    return render(request, template_name, {'form': form})


@login_required
def timetable_update(request, pk):
    template_name = 'timetable/timetable_update.html'
    qs = get_object_or_404(Timetable, pk=pk)
    if request.method == 'POST':
        form = TimetabeForm(request.POST, request.FILES, instance=qs)
        print(form.errors.as_data())
        if form.is_valid():
            form.save()
            messages.success(request, 'Update succesfull.')
            return redirect('timetable:all')
    else:
        context = {'form': TimetabeForm(instance=qs)}
    return render(request, template_name, context)


@login_required
def timetable_delete(request, pk):
    qs = get_object_or_404(Timetable, pk=pk)
    template_name = 'timetable/timetable_delete.html'
    if request.method == 'POST':
        qs.delete()
        messages.success(request, 'Timetable successfully deleted.')
        return redirect('timetable:all')
    return render(request, template_name, {'obj': qs})
