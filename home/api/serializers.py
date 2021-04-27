from rest_framework import serializers
from home import models


class MentalFitnessAssesmentSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.MentalFitnessAssesment
		fields = ('date', 'o_confidence', 'o_concentration', 'o_composure', 'o_challenge',
				'o_commitment', 'total')


class JournalSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.Journal
		fields = ['user', 'date', 'text']