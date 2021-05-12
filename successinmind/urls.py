"""successinmind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
	https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('home.urls')),

	path('api-auth/', include('rest_framework.urls'), name='rest_framework'),


	path('cn4/', include('cn4.urls'))
]


# Hello,
# If you are reading this you are on quite a journey. You are likely
# attempting to edit or add something to this website. That is a bold undertaking.
# This website is special to me. This is the first website I have ever built.
# While I knew python, I had never touched HTML, CSS, JS, or Django.
# The information I had to go off of to create this website was staggeringly poor.
# The "design documents" (aka. hand drawn scribbles) were at best ripe with 
# grammatical errors and poor formatting. At worst they were unreadable. I was
# lucky to have a few that were actually typed and not just pictures of scrap paper.
# I tried my best to keep this code neat, but I am just one man. A man who had three other classes
# and a part time job. This was supposed to be a group project, but none of my other teammates
# knew how to code. So it was just me. This was created over 3.5 sleepless weeks.
# Now it has been passed to you. I barely bothered to comment anything. Maybe you 
# will get a taste of the suffering I went through. Normally, I would not wish this on
# another, but it is 4 am right now and I want to bang my head into the wall.
# So good luck.
#   -- Maximilian Terenzi   <3


# P.S.  Tabs > Spaces
