from django.urls import path
from .import views
urlpatterns = [
    path('',views.signup),
    path('signuptask',views.signuptask),
    path('login',views.login),
    path('logintask',views.logintask),
    path('dashboard',views.dashboard),
    path('post',views.post),
   path("editprofile",views.editprofile),
    path('updatetask',views.updatetask),
    path('profile',views.profile)

]
