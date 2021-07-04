from django.urls import path

from home.api import views

urlpatterns = [
	path('', views.ApiMainView.as_view(), name='main_api'),
	path('user/', views.UserApiView.as_view(), name='user_api'),
	path('mfa/', views.MFAApiView.as_view(), name='mfa_api'),
	path('journal/', views.JournalApiView.as_view(), name='journal_api'),
	path('weekly_plan/', views.WeeklyPlanApiView.as_view(), name='weekly_plan_api'),
	path('mfa_team/', views.TeamMFAApiView.as_view(), name='team_mfa_api'),
]