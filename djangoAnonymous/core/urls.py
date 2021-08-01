
from django.urls import path
from . import views
app_name = 'core'
urlpatterns = [
    # should display a login/signup page so new users can create links for anyone to post messages for them , only registered users can view messages pertaning to em
    path('', views.home, name='home'),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('<str:user>/post', views.createMessage, name='createMessage'),
    path('post', views.createMessage, name='createMessage'),
    path('post/<str:user>', views.createMessage, name='createMessage'),
    path('view_post/', views.userDashboard, name='userDashboard'),

    #  Home page should have a link to login/signup or i should just redirect to the login page, then redirect to dashboard and copy link page

]
