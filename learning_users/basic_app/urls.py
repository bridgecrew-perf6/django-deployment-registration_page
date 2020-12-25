from django.urls import path
from . import views
app_name = 'basic_app'
urlpatterns=[

    path('', views.index, name='index'),
    path('registration/', views.registration, name='registration'),
    path('login/', views.user_login, name= 'user_login'),
    path('profile/', views.profile, name='profile')
]