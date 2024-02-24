from django.urls import path
from main import views, viewsNode

urlpatterns = [
    path('ws/<str:User_email>/<str:friend_email>/', views.my_websocket, name="chatUser"),
    path('chats/<str:user>/',views.render_list, name='chatList'),
    path('Profile/<str:user>/',views.render_profile, name='Profile'),
    path('updateForm/<str:user>/',views.render_update, name='Update'),
    path('deleteForm/<str:user>/',views.render_delete, name='DeleteForm'),
    path('deleteForm/<str:user>/delete/',views.delete_user),
    path('updateForm/<str:user>/update/',views.update_profile),
    path("allStudent/<str:user>/", viewsNode.redirect_GET_req_to_express, name="AllStundentsInfo"),
    path('updatePasswordForm/<str:user>/',views.render_patch, name='UpdatePassword'),
    path('updatePasswordForm/<str:user>/patch/',views.patch_profile),
]