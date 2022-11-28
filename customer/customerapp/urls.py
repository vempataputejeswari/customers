from django.urls import path
 
# importing views from views..py
from .views import create_view
from .views import list_view
from .views import detail_view
from .views import update_view
from .views import delete_view
urlpatterns = [
    path("customer/",create_view),
    path("list/", list_view),
    path('<id>', detail_view ),
    path('<id>/update', update_view ),
    path('<id>/delete',delete_view),
    
]