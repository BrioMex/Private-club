from django.shortcuts import render, redirect
from django.utils import timezone
from django.http import HttpResponseRedirect, HttpResponse, FileResponse

from .models import Event, Venue
from .forms import VenueForm, EventForm
import csv
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import letter

from django.core.paginator import Paginator

from calendar import HTMLCalendar


# Create your views here.
def home(request):
    return render(request, 'events/home.html', {}) #request always, which template are we going to, what are we sending there

def calendarmonth(request, year: int =int(timezone.now().year), month: int= int(timezone.now().month)):
    calendar_month=HTMLCalendar().formatmonth(theyear=year, themonth=month)
    return render(request, 'events/calendarmonth.html', {'year': year, 
                                                    'month': month, 'calendar_month':calendar_month})


def all_events(request):
    events_list = Event.objects.all().order_by('date')
    return render(request, 'events/events_list.html', {'events_list': events_list
                                                    })


def add_venue(request):
    submitted = False
    if request.method == "POST":
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_venue?submitted=True')

    else:
        form = VenueForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_venue.html',{'form': form, 'submitted': submitted})



def list_venues(request):
    #venues_list = Venue.objects.all().order_by('name')

    p = Paginator(Venue.objects.all().order_by('name'), 20)
    page = request.GET.get('page')
    venues_list = p.get_page(page)

    return render(request, 'events/venues.html', {'venues_list': venues_list
                                                    })

def show_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    return render(request, 'events/show_venue.html', {'venue': venue})

def search_venues(request):
    if request.method == "POST":
        searched = request.POST['searched']
        venues = Venue.objects.filter(name__contains = searched)
        return render(request, 'events/search_venues.html',{'searched': searched, 'venues': venues})
    else:
        return render(request, 'events/search_venues.html',{})


def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)
    if form.is_valid():
            form.save()
            return redirect('list-venue')

    return render(request, 'events/update_venue.html', {'venue': venue, 'form': form})


def add_event(request):
    submitted = False
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_event?submitted=True')

    else:
        form = EventForm
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'events/add_event.html',{'form': form, 'submitted': submitted})




def update_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    form = EventForm(request.POST or None, instance=event)
    if form.is_valid():
            form.save()
            return redirect('events-list')

    return render(request, 'events/update_event.html', {'event': event, 'form': form})


def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('events-list')

def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    existing = Event.objects.filter(venue =venue_id)
    if existing:
        pass
    else:
        venue.delete()
    return redirect('list-venue')

def venues_text(request):
    response = HttpResponse(content_type = 'text/plain')
    response['Content-Disposition'] = 'attachment, filename=venues.text'
    venues_list = Venue.objects.all().order_by('name')
    text_venues = []
    for venue in venues_list:
        text_venues.append(f'{venue.name}\n')
        text_venues.append(f'\t{venue.address}\n')
        text_venues.append(f'\t{venue.zip_code}\n')
        text_venues.append(f'\t{venue.phoneNumber}\n')
        text_venues.append(f'\t{venue.web}\n')
        text_venues.append(f'\t{venue.email}\n\n')
    response.writelines(text_venues)
    return response

def venues_csv(request):
    response = HttpResponse(content_type = 'text/csv')
    response['Content-Disposition'] = 'attachment, filename=venues.csv'
    writer = csv.writer(response)
    venues_list = Venue.objects.all().order_by('name')
    writer.writerow(['venue name','Adress','Zip Code','Phone Number','Web','Email'])
    for venue in venues_list:
        writer.writerow([venue.name,venue.address,venue.zip_code,venue.phoneNumber,venue.web,venue.email])
    return response


def venues_pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textobj = c.beginText(mm, mm)
    textobj.setTextOrigin(mm * 10,mm * 20)
    textobj.setFont("Helvetica",14)
    venues_list = Venue.objects.all().order_by('name')
    text_venues = []
    for venue in venues_list:
        text_venues.append(venue.name)
        text_venues.append("   "+str(venue.address))
        text_venues.append("   "+str(venue.zip_code))
        text_venues.append("   "+str(venue.phoneNumber))
        text_venues.append("   "+str(venue.web))
        text_venues.append("   "+str(venue.email))
        text_venues.append("   ")
    for line in text_venues:
        textobj.textLine(line)
    c.drawText(textobj)
    c.showPage()
    c.save()
    buf.seek(0)
    return FileResponse(buf, as_attachment=True, filename='venues.pdf')