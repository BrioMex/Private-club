from django.shortcuts import render
from django.utils import timezone

from .models import Event

from calendar import HTMLCalendar


# Create your views here.
def home(request):
    return render(request, 'events/home.html', {}) #request always, which template are we going to, what are we sending there

def calendarmonth(request, year: int =int(timezone.now().year), month: int= int(timezone.now().month)):
    calendar_month=HTMLCalendar().formatmonth(theyear=year, themonth=month)
    return render(request, 'events/calendarmonth.html', {'year': year, 
                                                    'month': month, 'calendar_month':calendar_month})


def all_events(request):
    events_list = Event.objects.all()
    return render(request, 'events/events_list.html', {'events_list': events_list
                                                    })