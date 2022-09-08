from django.contrib import admin


# Register your models here.
from .models import Venue, MyClubUser, Event
from .forms import RequiredInlineFormSet

class VenueInline(admin.TabularInline):
    model = Venue
    extra = 1
    formset = RequiredInlineFormSet # or AtLeastOneFormSet


class EventAdmin(admin.ModelAdmin):
    inlines = [
        VenueInline,
    ]
    # list_display = ("name","date", "venue", "manager") 
    # list_filter = ["date", "manager"]
    # search_fields = ["name"]



#admin.site.register(Venue)
admin.site.register(Event, EventAdmin)
admin.site.register(MyClubUser)