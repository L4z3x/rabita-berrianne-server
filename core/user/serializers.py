from rest_framework.serializers import ModelSerializer
from user.models import Participant, User


class ParticipantSerializer(ModelSerializer):
    class Meta:
        model = Participant
        fields = "__all__"


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ("id", "date_joined", "is_active", "is_staff")
        extra_kwargs = {
            "password": {"write_only": True},
            "email": {"required": True, "allow_blank": False},
        }
