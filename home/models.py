from django.contrib.auth.models import User
from django.db import models
from django.core import validators

# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	sports = models.CharField(max_length=256)
	gender = models.CharField(max_length=64)


class MentalFitnessAssessment(models.Model):
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	o_confidence = models.PositiveSmallIntegerField(default=0, null=True, validators=[
								validators.MinLengthValidator(0),
								validators.MaxLengthValidator(10),])
	o_concentration = models.PositiveSmallIntegerField(default=0, null=True, validators=[
								validators.MinLengthValidator(0),
								validators.MaxLengthValidator(10),])
	o_composure = models.PositiveSmallIntegerField(default=0, null=True, validators=[
								validators.MinLengthValidator(0),
								validators.MaxLengthValidator(10),])
	o_challenge = models.PositiveSmallIntegerField(default=0, null=True, validators=[
								validators.MinLengthValidator(0),
								validators.MaxLengthValidator(10),])
	o_commitment = models.PositiveSmallIntegerField(default=0, null=True, validators=[
								validators.MinLengthValidator(0),
								validators.MaxLengthValidator(10),])
	total = models.PositiveSmallIntegerField(default=0, null=True, validators=[
								validators.MinLengthValidator(0),
								validators.MaxLengthValidator(50),])

	def __str__(self) -> str:
		info = f'{self.user.email} - {str(self.date)}'
		return info


class Confidence(models.Model):
	mfa_id = models.ForeignKey('home.MentalFitnessAssessment', on_delete=models.CASCADE)
	confidence_1 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	confidence_2 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	confidence_3 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	confidence_4 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	confidence_5 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	p_confidence = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(10),
									])


class Composure(models.Model):
	mfa_id = models.ForeignKey('home.MentalFitnessAssessment', on_delete=models.CASCADE)
	composure_1 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	composure_2 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	composure_3 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	composure_4 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	composure_5 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	p_composure = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(10),
									])


class Challenge(models.Model):
	mfa_id = models.ForeignKey('home.MentalFitnessAssessment', on_delete=models.CASCADE)
	challenge_1 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	challenge_2 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	challenge_3 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	challenge_4 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	challenge_5 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	p_challenge = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(10),
									])


class Concentration(models.Model):
	mfa_id = models.ForeignKey('home.MentalFitnessAssessment', on_delete=models.CASCADE)
	concentration_1 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	concentration_2 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	concentration_3 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	concentration_4 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	concentration_5 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	p_concentration = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(10),
									])


class Commitment(models.Model):
	mfa_id = models.ForeignKey('home.MentalFitnessAssessment', on_delete=models.CASCADE)
	commitment_1 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	commitment_2 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	commitment_3 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	commitment_4 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	commitment_5 = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(2),
									])
	p_commitment = models.PositiveSmallIntegerField(null=False, 
									validators=[
										validators.MinLengthValidator(0),
										validators.MaxLengthValidator(10),
									])


class Journal(models.Model):
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	date = models.DateTimeField()
	text = models.TextField(max_length=2048)
