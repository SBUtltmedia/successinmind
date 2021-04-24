from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


# Create your views here.
from home import forms
from home import models


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
		if self.validate_post(request_values) and form.is_valid():
			user = form.save(commit=False)
			user.set_password(user.password)
			user.save()
			login(request, user)
			return redirect('home:index')
		return render(request, self.template_name, context={'failed': self.fail_msg})

	def validate_post(self, request_values):
		passed = True
		if len(request_values['first_name']) < 1:
			self.fail_msg.append('Please input a First Name!')
			passed = False
		if len(request_values['last_name']) < 1:
			self.fail_msg.append('Please input a Last Name!')
			passed = False
		if len(request_values['last_name']) < 1:
			self.fail_msg.append('Please input an Email Address!')
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
			self.fail_msg.append('Please input a Password!')
			passed = False
		return passed



class MFAView(TemplateView):
	template_name = 'MFA.html'

	def post(self, request, *args, **kwargs):
		request_values = request.POST.copy()
		for c in request_values.values():
			if not c:
				return
		mfa = models.MentalFitnessAssesment(user=request.user)
		mfa.save()

		self.gather_confidence(request_values, mfa)
		self.gather_composure(request_values, mfa)
		self.gather_challenge(request_values, mfa)
		self.gather_concentration(request_values, mfa)
		self.gather_commitment(request_values, mfa)

	def gather_confidence(self, request_values, mfa):
		c = models.Confidence(mfa_id=mfa)
		c.confidence_1 = request_values['confidence_1']
		c.confidence_2 = request_values['confidence_2']
		c.confidence_3 = request_values['confidence_3']
		c.confidence_4 = request_values['confidence_4']
		c.confidence_5 = request_values['confidence_5']
		c.save()

	def gather_composure(self, request_values, mfa):
		c = models.Composure(mfa_id=mfa)
		c.composure_1 = request_values['composure_1']
		c.composure_2 = request_values['composure_2']
		c.composure_3 = request_values['composure_3']
		c.composure_4 = request_values['composure_4']
		c.composure_5 = request_values['composure_5']
		c.save()

	def gather_challenge(self, request_values, mfa):
		c = models.Challenge(mfa_id=mfa)
		c.challenge_1 = request_values['challenge_1']
		c.challenge_2 = request_values['challenge_2']
		c.challenge_3 = request_values['challenge_3']
		c.challenge_4 = request_values['challenge_4']
		c.challenge_5 = request_values['challenge_5']
		c.save()

	def gather_concentration(self, request_values, mfa):
		c = models.Concentration(mfa_id=mfa)
		c.concentration_1 = request_values['concentration_1']
		c.concentration_2 = request_values['concentration_2']
		c.concentration_3 = request_values['concentration_3']
		c.concentration_4 = request_values['concentration_4']
		c.concentration_5 = request_values['concentration_5']
		c.save()

	def gather_commitment(self, request_values, mfa):
		c = models.Commitment(mfa_id=mfa)
		c.commitment_1 = request_values['commitment_1']
		c.commitment_2 = request_values['commitment_2']
		c.commitment_3 = request_values['commitment_3']
		c.commitment_4 = request_values['commitment_4']
		c.commitment_5 = request_values['commitment_5']
		c.save()


# class MFAReView(TemplateView):
# 	template_name = 'index.html'