"""habits URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import habits.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listhabits/', views.getHabits),
    path('addhabits/', views.addHabits),
    path('updatehabit/', views.updateHabit),
    path('streak/<habitid>', views.streak),
    path('streak_test/<habitid>', views.streak_test),
    path('sameperiodicity/', views.sameperiodicity),
    path('longrunnstreak/', views.longrunnstreak),
    path('longrunstreakforhabit/<habitid>', views.longrunstreakforhabit),
    path('struggling/', views.struggling),
    path('deletetestrecords/',views.deletehabits)

]
# Adding place holder