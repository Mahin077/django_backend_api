from django.urls import path
from tablecrud import views
from .views import PersonDetails,PersonInfo

urlpatterns = [
    path("person/",PersonDetails.as_view(),name="person"),
    path('person/<int:id>/',PersonInfo.as_view())
]
