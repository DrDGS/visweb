from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('opengl', views.opengl),
    path('threedmax', views.threedmax),
    path('ue', views.ue),
    path('unity', views.unity)
]
