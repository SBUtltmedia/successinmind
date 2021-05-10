from django.urls import path, include

from home import views

app_name = 'home'

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('login/', views.LogInView.as_view(), name='login'),
	path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
	path('MFA/', views.MFAView.as_view(), name='MFA'),
	path('logout/', views.user_logout, name='logout'),
	path('profile/', views.ProfileView.as_view(), name='profile'),
	path('teams/', views.TeamsView.as_view(), name='teams'),
	path('B_60/', views.B_60View.as_view(), name='B_60'),
	path('about/', views.AboutView.as_view(), name='about'),
	path('consultation/', views.ConsultationView.as_view(), name='consultation'),
	path('mind_gym/', views.MindGymView.as_view(), name='mind_gym'),

	# Export MFA
	path('export_mfa/<int:pk>/', views.ExportMFA.as_view(), name='export_mfa'),

	## Library ##
	path('library/', views.LibraryView.as_view(), name='library'),	
	# Media
	path('library/media/tutorials', views.TutorialsView.as_view(), name='library_media_tutorials'),
	path('library/media/articles', views.ArticlesView.as_view(), name='library_media_articles'),
	path('library/media/worksheets', views.WorksheetsView.as_view(), name='library_media_worksheets'),
	path('library/media/audio', views.AudioView.as_view(), name='library_media_audio'),
	path('library/media/videos', views.VideosView.as_view(), name='library_media_videos'),
	# Topic
	path('library/topic/overall_mental', views.OverallMentalView.as_view(), name='library_topic_overall_mental'),
	path('library/topic/ideal_performance', views.IdealPerformanceView.as_view(), name='library_topic_ideal_performance'),
	path('library/topic/mindfullness_meditation', views.MindfullnessMeditationView.as_view(), name='library_topic_mindfullness_meditation'),
	path('library/topic/sleep_rest', views.SleepRestView.as_view(), name='library_topic_sleep_rest'),
	path('library/topic/healing_recovery', views.HealingRecoveryView.as_view(), name='library_topic_healing_recovery'),
	path('library/topic/managing_thoughts_feelings', views.ManagingThoughtsFeelingsView.as_view(), name='library_topic_managing_thoughts_feelings'),

	path('api/', include('home.api.urls'), name='api')
]