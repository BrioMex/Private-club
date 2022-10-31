# First form not empty and can not be deleted
from django.forms.models import BaseInlineFormSet    

class RequiredInlineFormSet(BaseInlineFormSet):
    def _construct_form(self, i, **kwargs):
        form = super(RequiredInlineFormSet, self)._construct_form(i, **kwargs)
        if i < 1:
            form.empty_permitted = False
        return form

from django import forms
from django.forms import ModelForm
from .models import Venue, Event


#create a Venue form
class VenueForm(ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'zip_code', 'phoneNumber', 'web', 'email')

class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'date', 'manager', 'description', 'attendees', 'venue')
        labels = {
            'name' : 'name',
            'date' : 'Date (YYYY-MM-DD HH:MM:SS)',
            'manager' : 'Manager',
            'description' : 'description',
            'attendees' : 'attendees',
            'venue' : 'Venue',
        }