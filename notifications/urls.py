from django.urls import path 
from .views import (
    NotificationListAPIView,
    NotificationDetailAPIView,
    NotificationCreateAPIView,
    NotificationUpdateAPIView,
    NotificationDeleteAPIView,
    NotificationMarkReadAPIView,
    NotificationUnreadCountAPIView,
    NotificationMarkAllReadAPIView,
)

urlpatterns = [
    path('', NotificationListAPIView.as_view(), name='notification-list'),
    path('<int:pk>/', NotificationDetailAPIView.as_view(), name='notification-detail'),
    path('create/', NotificationCreateAPIView.as_view(), name='notification-create'),
    path('<int:pk>/update/', NotificationUpdateAPIView.as_view(), name='notification-update'),
    path('<int:pk>/delete/', NotificationDeleteAPIView.as_view(), name='notification-delete'),
    path("<int:pk>/read/",NotificationMarkReadAPIView.as_view(),name="notification-read"),
    path(
    "unread-count/",
    NotificationUnreadCountAPIView.as_view(),
    name="notification-unread-count",
),
    path(
    "read-all/",
    NotificationMarkAllReadAPIView.as_view(),
    name="notification-read-all",
),
]
