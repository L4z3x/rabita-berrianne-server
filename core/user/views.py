from rest_framework.generics import CreateAPIView, ListAPIView
from user.models import Participant
from rest_framework.permissions import AllowAny
from drf_spectacular.utils import extend_schema
from user.serializers import ParticipantSerializer


@extend_schema(
    description="API view to create a participant.",
    summary="Create Participant",
    request=ParticipantSerializer,
    responses={201: ParticipantSerializer, 400: "Bad Request"},
    operation_id="create-participant",
)
class CreateParticipantView(CreateAPIView):
    """
    API view to handle participant-related operations.
    """

    authentication_classes = []
    permission_classes = [AllowAny]
    serializer_class = ParticipantSerializer


@extend_schema(
    description="to get a specific participant, use the id parameter in the URL, or simply use the endpoint to list all participants.",
    summary="List Participant",
    request=ParticipantSerializer,
    responses={200: ParticipantSerializer, 400: "Bad Request"},
    operation_id="list-participant",
    parameters=[
        {
            "name": "id",
            "in": "query",
            "description": "Participant ID to retrieve specific participant",
            "required": False,
            "type": "integer",
        }
    ],
)
class ListParticipantView(ListAPIView):
    """
    API view to list all participants.
    """

    queryset = Participant.objects.all()
    permission_classes = [AllowAny]
    serializer_class = ParticipantSerializer

    def get_object(self):
        id = self.kwargs.get("id", None)
        if id:
            return Participant.objects.filter(id=id).first()
        else:
            return None

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("id", None)
        if id:
            return self.get(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)
