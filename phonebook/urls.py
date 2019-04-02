from django.urls import path
from django.contrib.auth import views as auth_views
from .import views

from .views import ContactListView

app_name = "phonebook"

urlpatterns = [
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),

    path('signup', views.signup, name='signup'),
    path('', views.ContactListView.as_view(), name='contact-index'),
    path('add-contact', views.ContactCreateView.as_view(), name='add-contact'),
    path('<int:pk>/update-contact', views.ContactUpdateView.as_view(), name='update-contact'),
    path('<int:pk>/delete-contact', views.ContactDeleteView.as_view(), name='delete-contact'),
    ]