from django.urls import path
from movies import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('index/', views.IndexView.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path("register/", views.RegisterView.as_view(), name="register")
]

htmx_urlpatterns = [
    path('check-username/', views.check_username, name='check-usesrname')
]


urlpatterns += htmx_urlpatterns