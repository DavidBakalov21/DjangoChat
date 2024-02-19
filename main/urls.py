from django.urls import path
from main import views

urlpatterns = [
    path('ws/<str:User_email>/<str:friend_email>/', views.my_websocket, name="chatUser"),
    path('chats/<str:user>/',views.render_list, name='chatList'),
    path('Profile/<str:user>/',views.render_profile, name='Profile'),
    path('updateForm/<str:user>/',views.render_update, name='Update'),
    path('updateForm/<str:user>/update/',views.update_profile),
]