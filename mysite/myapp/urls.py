
from django.urls import path
from . import views

urlpatterns = [
    path('',views.first,name='first'),
    path('base/',views.base,name='base'),
    path('login/',views.login_user,name='login'),
    path('signup/',views.signup,name='signup'),
    path('about/',views.about ,name='about'),
    path('booking/',views.booking,name='booking'),
    path('department/',views.department,name='department'),
    path('doctors/',views.doctors,name='doctors'),
    path('career/',views.career_view,name='career'),
    path('contact/',views.contact,name='contact'),
]
