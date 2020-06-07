from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import AccomodationForm
from .models import Accomodation, Booking

# Create your views here.
@login_required
def accomodation_list(request):
    template_name = 'accomodation/accomodation_list.html'
    accommodation_list = Accomodation.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(accommodation_list, 5)
    qs = paginator.get_page(page)
    context = {
        'obj': qs
    }
    return render(request, template_name, context)


@login_required
def accomodation_create(request):
    template_name = 'accomodation/accomodation_create.html'
    if request.method == "POST":
        form = AccomodationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Accomodation house successfully added.')
            return redirect(reverse('accomodation:accomodation_list'))
    else:
        form = AccomodationForm()
    return render(request, template_name, {'form': form})


@login_required
def accomodation_details(request, pk):
    template_name = 'accomodation/accomodation_details.html'
    qs = get_object_or_404(Accomodation, pk=pk)
    ps = Booking.objects.filter(accomodation=pk)
    context = {
        'obj': qs,
        'res': ps
    }
    return render(request, template_name, context)


@login_required
def update_accommodation(request, pk):
    template_name = 'accomodation/accomodation_edit.html'
    qs = get_object_or_404(Accomodation, pk=pk)
    if request.method == 'POST':
        form = AccomodationForm(request.POST, instance=qs)
        print(form.errors.as_data())
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated.')
            return redirect('accomodation:accomodation_list')
    else:
        context = {'form': AccomodationForm(instance=qs)}
    return render(request, template_name, context)


@login_required
def accomodation_delete(request, pk):
    qs = get_object_or_404(Accomodation, pk=pk)
    template_name = 'accomodation/accomodation_detele.html'
    if request.method == 'POST':
        qs.delete()
        messages.success(request, 'Accommodation successfully deleted.')
        return redirect('accomodation:accomodation_list')
    return render(request, template_name, {'obj': qs})
