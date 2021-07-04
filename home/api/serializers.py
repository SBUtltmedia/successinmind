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
		fields = ('user', 'date', 'training_goals', 'mental_fitness_goals',
		'course_work_goals', 'awesome_performance', 'great_practice',
		'feeling_happy', 'feeling_confident', 'good_rest', 'confidence',
		'concentration', 'composure', 'challenge_response', 'commitment',
		'overall_performance_rating', 'overall_satisfaction_rating')


class WeeklyPlanSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.WeeklyPlan
		fields = ('user', 'date', 'vision', 'training_goals', 'mental_fitness_goals',
		'course_work_goals', 'recreational_goals', 'goal_for_overall_performance_rating',
		'goal_for_level_of_satisfaction')



class TeamMentalFitnessAssessment(serializers.ModelSerializer):
	class Meta:
		model = models.Team_MentalFitnessAssessment
		fields = ('coach', 'name', 'code')