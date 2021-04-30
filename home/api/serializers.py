from rest_framework import serializers
from django.contrib.auth.models import User
from home import models


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username', 'email', 'first_name', 'last_name', 'password')

class MentalFitnessAssessmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.MentalFitnessAssessment
		fields = ('date', 'o_confidence', 'o_concentration', 'o_composure', 'o_challenge',
				'o_commitment', 'total')


class JournalSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Journal
		fields = ['user', 'date', 'text']