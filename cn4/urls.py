from django.urls import path, include

from cn4 import views

app_name = 'cn4'

urlpatterns = [
	path('', views.CN4View.as_view()),
]