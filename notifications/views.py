from django.shortcuts import render
from rest_framework import generics
from .models import Notification
from rest_framework.permissions import IsAuthenticated
from accounts.permissions import IsPlacementOfficer
from .serializers import NotificationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class NotificationListAPIView(generics.ListAPIView):

    serializer_class = NotificationSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(
            recipient=self.request.user
        ).select_related("recipient")

class NotificationDetailAPIView(generics.RetrieveAPIView):

    serializer_class = NotificationSerializer

    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(
            recipient=self.request.user
        ).select_related("recipient")


class NotificationCreateAPIView(generics.CreateAPIView):

    queryset = Notification.objects.select_related(
        "recipient"
    )

    serializer_class = NotificationSerializer

    permission_classes = [IsAuthenticated, IsPlacementOfficer]


class NotificationUpdateAPIView(generics.UpdateAPIView):

    queryset = Notification.objects.all()

    serializer_class = NotificationSerializer


class NotificationDeleteAPIView(generics.DestroyAPIView):

    queryset = Notification.objects.all()

    serializer_class = NotificationSerializer

class NotificationMarkReadAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):

        try:
            notification = Notification.objects.get(
                pk=pk,
                recipient=request.user
            )

        except Notification.DoesNotExist:

            return Response(
                {
                    "message": "Notification not found."
                },
                status=status.HTTP_404_NOT_FOUND
            )

        notification.is_read = True
        notification.save()

        return Response(
            {
                "message": "Notification marked as read."
            }
        )

class NotificationUnreadCountAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        unread_count = Notification.objects.filter(
            recipient=request.user,
            is_read=False
        ).count()

        return Response(
            {
                "unread_count": unread_count
            }
        )

class NotificationMarkAllReadAPIView(APIView):

    permission_classes = [IsAuthenticated]

    def patch(self, request):

        updated_count = Notification.objects.filter(
            recipient=request.user,
            is_read=False
        ).update(is_read=True)

        return Response(
            {
                "message": "All notifications marked as read.",
                "updated_notifications": updated_count
            },
            status=status.HTTP_200_OK
        )