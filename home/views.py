from django.contrib.auth.models import User
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render, redirect

from rest_framework.response import Response
from rest_framework import status



# Create your views here.
from home import forms
from home import models
from home import render_pdf


import decimal


@login_required
def user_logout(request):
	logout(request)
	return redirect('home:index')


class IndexView(TemplateView):
	template_name = 'index.html'


class LogInView(TemplateView):
	form_class = forms.LoginForm
	template_name = 'login.html'

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = authenticate(username=form.cleaned_data['email'],
							password=form.cleaned_data['password'])
			print('USER: ', user)
			if user is not None:
				login(request, user)
				return redirect('home:index')
		return render(request, self.template_name, context={'failed': True})


class SignUpView(TemplateView):
	form_class = forms.RegisterForm
	template_name = 'sign_up.html'

	def post(self, request, *args, **kwargs):
		self.fail_msg = []

		request_values = request.POST.copy()
		request_values['username'] = request_values['email']
		form = self.form_class(data=request_values)
		# Custom validation (Form wasn't too helpful here)
		if self.validate_post(request_values) and form.is_valid():
			user = form.save(commit=False)
			user.set_password(user.password)
			user.save()

			profile = models.Profile(user=user)
			profile.sports = request_values['sports']
			profile.gender = request_values['gender']
			profile.coach = True if request_values.get('coach', None) == 'on' else False

			profile.save()

			login(request, user)
			return redirect('home:index')
		return render(request, self.template_name, context={'failed': self.fail_msg})

	def validate_post(self, request_values):
		# Custom Validation

		passed = True
		if len(request_values['email']) > 1:
			if User.objects.filter(email=request_values['email']).exists():
				self.fail_msg.append('User already exists!')
				passed = False
		if len(request_values['first_name']) < 1:
			self.fail_msg.append('Please input a first name!')
			passed = False
		if len(request_values['last_name']) < 1:
			self.fail_msg.append('Please input a last name!')
			passed = False
		if len(request_values['last_name']) < 1:
			self.fail_msg.append('Please input an email address!')
			passed = False
		if len(request_values['password']) > 0:
			if request_values['password'] != request_values['c_password']:
				self.fail_msg.append('Passwords do not match!')
				passed = False
			else:
				if len(request_values['password']) < 8:
					self.fail_msg.append('Password must be 8+ characters!')
					passed = False
		else:
			self.fail_msg.append('Please input a password!')
			passed = False
		if len(request_values['gender']) < 0:
			self.fail_msg.append('Please input a gender!')
			passed = False
		if len(request_values['sports']) < 0:
			self.fail_msg.append('Please input a sport!')
			passed = False
		return passed


@method_decorator(login_required, name='dispatch')
class MFAView(TemplateView):
	template_name = 'MFA.html'

	def post(self, request, *args, **kwargs):
		request_values = request.POST.copy()
		for c in request_values.values():
			if not c:
				return
		mfa = models.MentalFitnessAssessment(user=request.user)
		mfa.save()

		try:
			results = {
				'Confidence': self.gather_confidence(request_values, mfa),
				'Concentration': self.gather_composure(request_values, mfa),
				'Composure': self.gather_challenge(request_values, mfa),
				'Challenge': self.gather_concentration(request_values, mfa),
				'Commitment': self.gather_commitment(request_values, mfa),
			}
		except:
			# Handled in time with JS, but just in case
			return render(request, self.template_name, context={'error': "Be sure to fill out every value!"})
		results_data = list(results.values())
		results_sum = sum(results_data)
		
		mfa.total = results_sum
		mfa.save()
		return render(request, self.template_name, context={'results': results.items(),
															'result_data': list(results.values()),
															'result_sum': results_sum,
															'result_percent': results_sum,
															})

	def gather_confidence(self, request_values, mfa):
		c = models.Confidence(mfa_id=mfa)
		c.confidence_1 = request_values['confidence_1']
		c.confidence_2 = request_values['confidence_2']
		c.confidence_3 = request_values['confidence_3']
		c.confidence_4 = request_values['confidence_4']
		c.confidence_5 = request_values['confidence_5']
		c.p_confidence = request_values['p_confidence']
		c.save()
		
		o_confidence = 0
		for i in range(1, 6):
			o_confidence += int(request_values[f'confidence_{i}'])
		o_confidence += int(request_values['p_confidence'])
		mfa.o_confidence = o_confidence
		mfa.save()

		return o_confidence

	def gather_composure(self, request_values, mfa):
		c = models.Composure(mfa_id=mfa)
		c.composure_1 = request_values['composure_1']
		c.composure_2 = request_values['composure_2']
		c.composure_3 = request_values['composure_3']
		c.composure_4 = request_values['composure_4']
		c.composure_5 = request_values['composure_5']
		c.p_composure = request_values['p_composure']
		c.save()

		o_composure = 0
		for i in range(1, 6):
			o_composure += int(request_values[f'composure_{i}'])
		o_composure += int(request_values['p_composure'])
		mfa.o_composure = o_composure
		mfa.save()

		return o_composure

	def gather_challenge(self, request_values, mfa):
		c = models.Challenge(mfa_id=mfa)
		c.challenge_1 = request_values['challenge_1']
		c.challenge_2 = request_values['challenge_2']
		c.challenge_3 = request_values['challenge_3']
		c.challenge_4 = request_values['challenge_4']
		c.challenge_5 = request_values['challenge_5']
		c.p_challenge = request_values['p_challenge']
		c.save()

		o_challenge = 0
		for i in range(1, 6):
			o_challenge += int(request_values[f'challenge_{i}'])
		o_challenge += int(request_values['p_challenge'])
		mfa.o_challenge = o_challenge
		mfa.save()

		return o_challenge

	def gather_concentration(self, request_values, mfa):
		c = models.Concentration(mfa_id=mfa)
		o_concentration = 0
		c.concentration_1 = request_values['concentration_1']
		c.concentration_2 = request_values['concentration_2']
		c.concentration_3 = request_values['concentration_3']
		c.concentration_4 = request_values['concentration_4']
		c.concentration_5 = request_values['concentration_5']
		c.p_concentration = request_values['p_concentration']
		c.save()

		o_concentration = 0
		for i in range(1, 6):
			o_concentration += int(request_values[f'concentration_{i}'])
		o_concentration += int(request_values['p_concentration'])
		mfa.o_concentration = o_concentration
		mfa.save()

		return o_concentration

	def gather_commitment(self, request_values, mfa):
		c = models.Commitment(mfa_id=mfa)
		c.commitment_1 = request_values['commitment_1']
		c.commitment_2 = request_values['commitment_2']
		c.commitment_3 = request_values['commitment_3']
		c.commitment_4 = request_values['commitment_4']
		c.commitment_5 = request_values['commitment_5']
		c.p_commitment = request_values['p_commitment']
		c.save()

		o_commitment = 0
		for i in range(1, 6):
			o_commitment += int(request_values[f'commitment_{i}'])
		o_commitment += int(request_values['p_commitment'])
		mfa.o_commitment = o_commitment
		mfa.save()

		return o_commitment



class MFA_Team_Selection_View(TemplateView):
	template_name = 'MFA_team_select.html'

	def post(self, request, *args, **kwargs):
		if request.POST.get('team_token', None):
			context = {
				'team_code': request.POST.get('team_token')
			}
			return render(request, 'MFA.html', context)

		request_values = request.POST.copy()
		for c in request_values.values():
			if not c:
				return
		mfa = models.MentalFitnessAssessment(user=request.user)
		team_code = request.POST.get('team_code')
		mfa.team = models.Team_MentalFitnessAssessment.objects.get(team_code=team_code) 
		mfa.save()

		try:
			results = {
				'Confidence': self.gather_confidence(request_values, mfa),
				'Concentration': self.gather_composure(request_values, mfa),
				'Composure': self.gather_challenge(request_values, mfa),
				'Challenge': self.gather_concentration(request_values, mfa),
				'Commitment': self.gather_commitment(request_values, mfa),
			}
		except:
			# Handled in time with JS, but just in case
			return render(request, self.template_name, context={'error': "Be sure to fill out every value!"})
		results_data = list(results.values())
		results_sum = sum(results_data)
		
		mfa.total = results_sum
		mfa.save()
		context = {
			'results': results.items(),
			'result_data': list(results.values()),
			'result_sum': results_sum,
			'result_percent': results_sum,
			'team_code': request.POST.get('team_code')
		}
		return render(request, 'MFA.html', context=context)

	def gather_confidence(self, request_values, mfa):
		c = models.Confidence(mfa_id=mfa)
		c.confidence_1 = request_values['confidence_1']
		c.confidence_2 = request_values['confidence_2']
		c.confidence_3 = request_values['confidence_3']
		c.confidence_4 = request_values['confidence_4']
		c.confidence_5 = request_values['confidence_5']
		c.p_confidence = request_values['p_confidence']
		c.save()
		
		o_confidence = 0
		for i in range(1, 6):
			o_confidence += int(request_values[f'confidence_{i}'])
		o_confidence += int(request_values['p_confidence'])
		mfa.o_confidence = o_confidence
		mfa.save()

		return o_confidence

	def gather_composure(self, request_values, mfa):
		c = models.Composure(mfa_id=mfa)
		c.composure_1 = request_values['composure_1']
		c.composure_2 = request_values['composure_2']
		c.composure_3 = request_values['composure_3']
		c.composure_4 = request_values['composure_4']
		c.composure_5 = request_values['composure_5']
		c.p_composure = request_values['p_composure']
		c.save()

		o_composure = 0
		for i in range(1, 6):
			o_composure += int(request_values[f'composure_{i}'])
		o_composure += int(request_values['p_composure'])
		mfa.o_composure = o_composure
		mfa.save()

		return o_composure

	def gather_challenge(self, request_values, mfa):
		c = models.Challenge(mfa_id=mfa)
		c.challenge_1 = request_values['challenge_1']
		c.challenge_2 = request_values['challenge_2']
		c.challenge_3 = request_values['challenge_3']
		c.challenge_4 = request_values['challenge_4']
		c.challenge_5 = request_values['challenge_5']
		c.p_challenge = request_values['p_challenge']
		c.save()

		o_challenge = 0
		for i in range(1, 6):
			o_challenge += int(request_values[f'challenge_{i}'])
		o_challenge += int(request_values['p_challenge'])
		mfa.o_challenge = o_challenge
		mfa.save()

		return o_challenge

	def gather_concentration(self, request_values, mfa):
		c = models.Concentration(mfa_id=mfa)
		o_concentration = 0
		c.concentration_1 = request_values['concentration_1']
		c.concentration_2 = request_values['concentration_2']
		c.concentration_3 = request_values['concentration_3']
		c.concentration_4 = request_values['concentration_4']
		c.concentration_5 = request_values['concentration_5']
		c.p_concentration = request_values['p_concentration']
		c.save()

		o_concentration = 0
		for i in range(1, 6):
			o_concentration += int(request_values[f'concentration_{i}'])
		o_concentration += int(request_values['p_concentration'])
		mfa.o_concentration = o_concentration
		mfa.save()

		return o_concentration

	def gather_commitment(self, request_values, mfa):
		c = models.Commitment(mfa_id=mfa)
		c.commitment_1 = request_values['commitment_1']
		c.commitment_2 = request_values['commitment_2']
		c.commitment_3 = request_values['commitment_3']
		c.commitment_4 = request_values['commitment_4']
		c.commitment_5 = request_values['commitment_5']
		c.p_commitment = request_values['p_commitment']
		c.save()

		o_commitment = 0
		for i in range(1, 6):
			o_commitment += int(request_values[f'commitment_{i}'])
		o_commitment += int(request_values['p_commitment'])
		mfa.o_commitment = o_commitment
		mfa.save()

		return o_commitment



@method_decorator(login_required, name='dispatch')
class ProfileView(TemplateView):
	template_name = 'profile.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		user = self.request.user
		context['MFAs'] = self.percentize(models.MentalFitnessAssessment.objects.filter(user=user))
		context['profile'] = user.profile
		context['coach'] = user.profile.coach
		context['journals'] = models.Journal.objects.filter(user=user)
		context['weekly_plans'] = models.WeeklyPlan.objects.filter(user=user)
		context['teams'] = self.get_team_context(user)
		return context

	def post(self, request, *args, **kwargs):
		team = models.Team_MentalFitnessAssessment(coach=request.user)
		request_values = request.POST.copy()
		team.name = request_values['team_name']
		team.team_code = request_values['team_token']
		team.save()

		return render(request, self.template_name, context=self.get_context_data())


	def percentize(self, mfas):
		_mfas = []
		for mfa in mfas:
			_dict = {}
			_dict['date'] = mfa.date
			_dict['o_confidence'] = (mfa.o_confidence / 20) * 100
			_dict['o_concentration'] = (mfa.o_concentration / 20) * 100
			_dict['o_composure'] = (mfa.o_composure / 20) * 100
			_dict['o_challenge'] = (mfa.o_challenge / 20) * 100
			_dict['o_commitment'] = (mfa.o_commitment / 20) * 100
			_dict['total'] = mfa.total
			_dict['pk'] = mfa.pk
			_mfas.append(_dict)
		return _mfas

	def get_team_context(self, user):
		teams = models.Team_MentalFitnessAssessment.objects.filter(coach=user)
		teams_data = []
		for team in teams:
			team_data = {
				'name': team.name,
				'code': team.team_code,
				'submissions': 0,
				'a_confidence': 0,
				'a_concentration': 0,
				'a_composure': 0,
				'a_challenge': 0,
				'a_commitment': 0,
				'a_total': 0,
			}
			mfas = models.MentalFitnessAssessment.objects.filter(team=team)
			team_data['submissions'] = len(mfas)
			if len(mfas) > 0:
				for mfa in mfas:
					team_data['a_confidence'] += mfa.o_confidence
					team_data['a_concentration'] += mfa.o_concentration
					team_data['a_composure'] += mfa.o_composure
					team_data['a_challenge'] += mfa.o_challenge
					team_data['a_commitment'] += mfa.o_commitment
					team_data['a_total'] += mfa.total
				team_data['a_confidence'] /= len(mfas)
				team_data['a_concentration'] /= len(mfas)
				team_data['a_composure'] /= len(mfas)
				team_data['a_challenge'] /= len(mfas)
				team_data['a_commitment'] /= len(mfas)
				team_data['a_total'] /= len(mfas)

				team_data['a_confidence'] = (team_data['a_confidence'] / 20) * 100
				team_data['a_concentration'] =(team_data['a_concentration'] / 20) * 100
				team_data['a_composure'] = (team_data['a_composure'] / 20) * 100
				team_data['a_challenge'] = (team_data['a_challenge'] / 20) * 100
				team_data['a_commitment'] = (team_data['a_commitment'] / 20) * 100
			teams_data.append(team_data)
		return teams_data


@method_decorator(login_required, name='dispatch')
class ExportMFA(View):

	def get(self, request, pk):
		mfa = models.MentalFitnessAssessment.objects.get(pk=pk)
		if mfa.user == request.user:
			data = {
				'mfa': mfa,
				'confidence': models.Confidence.objects.filter(mfa_id=mfa)[0],
				'concentration': models.Concentration.objects.filter(mfa_id=mfa)[0],
				'composure': models.Composure.objects.filter(mfa_id=mfa)[0],
				'challenge': models.Challenge.objects.filter(mfa_id=mfa)[0],
				'commitment': models.Commitment.objects.filter(mfa_id=mfa)[0],
			}
			return render_pdf.Render.render('MFA_export.html', data)
		else:
			return render_pdf.Render.render('MFA_export.html', {})



class B_60View(TemplateView):
	template_name = 'b_60.html'


class TeamsView(TemplateView):
	template_name = 'teams.html'


class AboutView(TemplateView):
	template_name = 'about.html'


class ConsultationView(TemplateView):
	template_name = 'consultation.html'



class MindGymView(TemplateView):
	template_name = 'mind_gym.html'



## Library Views ##

# Media Format

class LibraryView(TemplateView):
	template_name = 'library.html'


class TutorialsView(TemplateView):
	template_name = 'library/media/tutorials.html'


class ArticlesView(TemplateView):
	template_name = 'library/media/articles.html'


class WorksheetsView(TemplateView):
	template_name = 'library/media/worksheets.html'


class AudioView(TemplateView):
	template_name = 'library/media/audio.html'


class VideosView(TemplateView):
	template_name = 'library/media/videos.html'

# End Media

# Topic

class OverallMentalView(TemplateView):
	template_name = 'library/topic/overall_mental.html'


class IdealPerformanceView(TemplateView):
	template_name = 'library/topic/ideal_performance.html'


class MindfullnessMeditationView(TemplateView):
	template_name = 'library/topic/mindfullness_meditation.html'


class SleepRestView(TemplateView):
	template_name = 'library/topic/sleep_rest.html'


class HealingRecoveryView(TemplateView):
	template_name = 'library/topic/healing_recovery.html'



class ManagingThoughtsFeelingsView(TemplateView):
	template_name = 'library/topic/managing_thoughts_feelings.html'

# End Topic

## End Library