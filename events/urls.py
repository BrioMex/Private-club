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
]
