from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("chat/<str:sender>/<str:receiver>", views.chat, name="chat"),
    path("savemess/", views.savemess, name="savemess"),
    path('messages/<int:sender>/<int:receiver>', views.messages, name='messages'),
    ]