from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    #path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('delete/', views.delete, name='delete'),
    path('profile/<int:pk>', views.profile, name='profile'),
    path('edit/<str:user>', views.edit, name='edit'),
]