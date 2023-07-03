from django.urls import path
from .views import UserItemsViews

urlpatterns = [
    path('user-items/', UserItemsViews.as_view()),
    path('user-items/<int:id>', UserItemsViews.as_view())
]