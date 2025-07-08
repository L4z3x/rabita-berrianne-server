from django.urls import path
from user.views import CreateParticipantView, ListParticipantView

urlpatterns = [
    path(
        "create/",
        CreateParticipantView.as_view(),
        name="create-participant",
    ),
    path("", ListParticipantView.as_view(), name="list-participant"),
]
