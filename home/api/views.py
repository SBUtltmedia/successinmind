from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from home.api import serializers
from home import models


class ApiMainView(APIView):

	def get(self, response):
		return Response({
			'/api/mfa': ['GET - Returns all MFAs by User (Filterable by \'date\')'],
			'/api/journal': [
				'GET - Returns all Journals by User (Filterable by \'date\')',
				'POST - Creates new Journal record. Requires \'date\', \'text\'',
				'DELETE - Deletes Journal record of user. Requires \'date\'',
			]
			})



class UserApiView(APIView):

	def post(self, request, *args, **kwargs):
		data = {
			'username': request.data.get('email'),
			'email': request.data.get('email'),
			'first_name': request.data.get('first_name'),
			'last_name': request.data.get('last_name'),
			'password': request.data.get('password'),
		}
		sports = request.data.get('sports')
		gender = request.data.get('gender')
		serializer = serializers.JournalSerializer(data=data)
		if serializer.is_valid():
			user = serializer.save()
			
			profile = models.Profile(user=user)
			profile.sports = sports
			profile.gender = gender
			profile.save()

			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MFAApiView(APIView):
	permission_classes = [permissions.IsAuthenticated]

	def get(self, request, *args, **kwargs):
		date = request.data.get('date')
		if date:
			mfa = models.MentalFitnessAssessment.objects.filter(user=request.user, date=date)
		else:
			mfa = models.MentalFitnessAssessment.objects.filter(user=request.user)
		serializer = serializers.MentalFitnessAssessmentSerializer(mfa, many=True)

		return Response(serializer.data, status=status.HTTP_200_OK)


class JournalApiView(APIView):
	permission_classes = [permissions.IsAuthenticated]

	def get(self, request, *args, **kwargs):
		date = request.data.get('date')
		if date:
			journal = models.Journal.objects.filter(user=request.user, date=date)
		else:
			journal = models.Journal.objects.filter(user=request.user)
		serializer = serializers.JournalSerializer(journal, many=True)

		return Response(serializer.data, status=status.HTTP_200_OK)

	def post(self, request, *args, **kwargs):
		data = {
			'user': request.user.id,
			'date': request.data.get('date'),
			'text': request.data.get('text'),
		}
		serializer = serializers.JournalSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		else:
			return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, *args, **kwargs):
		data = {
			'user': request.user.id,
			'date': request.data.get('date')
		}

		journal = models.Journal.objects.filter(user=data['user'], date=data['date'])
		if journal:
			journal.delete()
			return Response(status=status.HTTP_200_OK)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)
