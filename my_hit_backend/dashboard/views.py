from django.shortcuts import render
from accounts.models import User
from queries.models import Query
from events.models import Event
from accommodation.models import Accomodation
# Create your views here.


def home(request):
    template_name = 'dashboard/home.html'
    users = User.objects.all().exclude(is_superuser=True).count()
    quries = Query.objects.all().count()
    events = Event.objects.all().count()
    accomodation = Accomodation.objects.all().count()

    context = {
        'users': users,
        'quries': quries,
        'events': events,
        'accomodation': accomodation
    }
    return render(request, template_name, context)
