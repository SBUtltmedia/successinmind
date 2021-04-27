from django.urls import path

from home.api import views

urlpatterns = [
	path('', views.ApiMainView.as_view(), name='main_api'),
	path('mfa/', views.MFAApiView.as_view(), name='mfa_api'),
	path('journal/', views.JournalApiView.as_view(), name='journal_api'),
]