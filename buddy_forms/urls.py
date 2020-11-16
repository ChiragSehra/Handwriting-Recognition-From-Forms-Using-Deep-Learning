from django.urls import path
from buddy_forms import views

app_name = "rest_api"


urlpatterns = [
    path("form_links/", views.form_links),
]
