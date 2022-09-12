from django.contrib import admin


# Register your models here.
from .models import Venue, MyClubUser, Event
from .forms import RequiredInlineFormSet

# class VenueInline(admin.TabularInline):
#     model = Venue
#     extra = 1
#     formset = RequiredInlineFormSet # or AtLeastOneFormSet


# class EventAdmin(admin.ModelAdmin):
#     inlines = [
#         VenueInline,
#     ]
    # list_display = ("name","date", "venue", "manager") 
    # list_filter = ["date", "manager"]
    # search_fields = ["name"]



#admin.site.register(Venue)
@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phoneNumber')
    ordering = ('name',)
    search_fields = ('name',)


@admin.register(Event)#, EventAdmin)
class EventAdmin(admin.ModelAdmin):
    fields = (('name', 'venue'), 'date', 'description', 'manager', 'attendees')
    list_display = ('name', 'venue', 'date')
    list_filter = ('date', 'venue',)
    ordering = ('date',)


admin.site.register(MyClubUser)