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


class MFAApiView(APIView):
	permission_classes = [permissions.IsAuthenticated]

	def get(self, request, *args, **kwargs):
		date = request.data.get('date')
		if date:
			mfa = models.MentalFitnessAssesment.objects.filter(user=request.user, date=date)
		else:
			mfa = models.MentalFitnessAssesment.objects.filter(user=request.user)
		serializer = serializers.MentalFitnessAssesmentSerializer(mfa, many=True)

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