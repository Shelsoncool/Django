
from django.urls import path
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from . import views
urlpatterns = [
    path('', views.indexView2, name="Home"),
    path('dashboard/',views.dashboardView,name="dashboard"),
    path('login/',LoginView.as_view(),name="login_urls"),
    path('register/',views.registerView,name="register_urls"),
    path('logout/',LogoutView.as_view(next_page='login_urls'),name="logout"),
]
