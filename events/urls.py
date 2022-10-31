from django.urls import path

from . import views #importing views for events app

urlpatterns = [
    path('', views.home, name = "home"), #first: defining url in browser, second: function or class name, third name assigned ofr easy calling
    path('calendar/',views.calendarmonth, name ='calendar'),
    path('calendar/<int:year>/<int:month>/',views.calendarmonth, name ='calendarmonth'),
    path('events/', views.all_events, name= "events-list"),
    path('add_venue', views.add_venue, name= "add-venue"),
    path('list_venues', views.list_venues, name= "list-venue"),
    path('show_venue/<int:venue_id>/', views.show_venue, name= "show-venue"),
    path('search_venues', views.search_venues, name= "search-venue"),
    path('update_venue/<int:venue_id>/', views.update_venue, name= "update-venue"),
    path('add_event', views.add_event, name= "add-event"),
    path('update_event/<int:event_id>/', views.update_event, name= "update-event"),
    path('delete_event/<int:event_id>/', views.delete_event, name = 'delete-event'),
    path('delete_venue/<int:venue_id>/', views.delete_venue, name = 'delete-venue'),
]
