from django.urls import path

from home import views

app_name = 'home'

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('login/', views.LogInView.as_view(), name='login'),
	path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
	path('MFA/', views.MFAView.as_view(), name='MFA'),
	path('logout/', views.user_logout, name='logout'),
]