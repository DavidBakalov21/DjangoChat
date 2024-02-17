from django.urls import path
from log_reg import views
urlpatterns = [
    path("register",views.render_sign_up, name='sign_up'),
    path("login",views.render_sign_in, name='sign_in'),
    path("signUp/",views.create_user),
    path("login/",views.login_user)
]