from django.contrib import admin
from django.urls import path, include
from tickets.views import ticket_list 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ticket_list, name='ticket_list'),
    path('tickets/', include('tickets.urls')),
]