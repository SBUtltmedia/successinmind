from django.db import models
from django.utils import timezone
from django.core import validators

# Create your models here.

class MentalFitnessAssesment(models.Model):
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self) -> str:
		return self.user.username + " - " + str(self.date)


class Confidence(models.Model):
	mfa_id = models.ForeignKey('home.MentalFitnessAssesment', on_delete=models.CASCADE)
	confidence_1 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])
	confidence_2 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])
	confidence_3 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])
	confidence_4 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])
	confidence_5 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])


class Composure(models.Model):
	mfa_id = models.ForeignKey('home.MentalFitnessAssesment', on_delete=models.CASCADE)
	composure_1 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])
	composure_2 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])
	composure_3 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])
	composure_4 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])
	composure_5 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])


class Challenge(models.Model):
	mfa_id = models.ForeignKey('home.MentalFitnessAssesment', on_delete=models.CASCADE)
	challenge_1 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])
	challenge_2 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])
	challenge_3 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])
	challenge_4 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])
	challenge_5 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])


class Concentration(models.Model):
	mfa_id = models.ForeignKey('home.MentalFitnessAssesment', on_delete=models.CASCADE)
	concentration_1 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])
	concentration_2 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])
	concentration_3 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])
	concentration_4 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])
	concentration_5 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])


class Commitment(models.Model):
	mfa_id = models.ForeignKey('home.MentalFitnessAssesment', on_delete=models.CASCADE)
	commitment_1 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])
	commitment_2 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])
	commitment_3 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])
	commitment_4 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])
	commitment_5 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(1),
										validators.MaxLengthValidator(3),
									])

