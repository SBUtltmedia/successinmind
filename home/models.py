from django.contrib.auth.models import User
from django.db import models
from django.core import validators

# Create your models here.


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	sports = models.CharField(max_length=256)
	gender = models.CharField(max_length=64)
	coach = models.BooleanField(default=False)


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
	training_goals = models.BooleanField()
	mental_fitness_goals = models.BooleanField()
	course_work_goals = models.BooleanField()
	awesome_performance = models.TextField(max_length=2048)
	great_practice = models.TextField(max_length=2048)
	feeling_happy = models.TextField(max_length=2048)
	feeling_confident = models.TextField(max_length=2048)
	good_rest = models.TextField(max_length=2048)
	confidence = models.PositiveSmallIntegerField()
	concentration = models.PositiveSmallIntegerField()
	composure = models.PositiveSmallIntegerField()
	challenge_response = models.PositiveSmallIntegerField()
	commitment = models.PositiveSmallIntegerField()
	overall_performance_rating = models.PositiveSmallIntegerField()
	overall_satisfaction_rating = models.PositiveSmallIntegerField()


class WeeklyPlan(models.Model):
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
	date = models.DateTimeField()
	vision = models.TextField(max_length=2048)
	training_goals = models.PositiveSmallIntegerField()
	mental_fitness_goals = models.PositiveSmallIntegerField()
	course_work_goals = models.PositiveSmallIntegerField()
	recreational_goals = models.PositiveSmallIntegerField()
	goal_for_overall_performance_rating = models.PositiveSmallIntegerField()
	goal_for_level_of_satisfaction = models.PositiveSmallIntegerField()

