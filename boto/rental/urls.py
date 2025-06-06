from django.urls import path

from . import views

app_name = "rental"
urlpatterns = [
    path("groups/", view=views.GroupView.as_view(), name="groups"),
]
