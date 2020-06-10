from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django import forms
from .models import *
from django.contrib.auth import get_user_model


class UserForm(UserCreationForm):

	class Meta:
		model = User
		fields = ['name', 'username']


	def clean_email(self):
		email = self.cleaned_data.get('email')

		# Valido o email para ser obrigatório
		if email == '':
			raise forms.ValidationError('O endereço de email é obrigatório.')
		return email

		if email and User.objects.filter(email=email).count():
			raise forms.ValidationError(
				'Este endereço de email já está em uso. Por favor, use um email diferente.')
		return email


