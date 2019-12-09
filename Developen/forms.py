from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class SignInForm(forms.Form):
	username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Username',
				'autocomplete': 'off'
			}
		))
	password = forms.CharField(label='Password', max_length=100, widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Password',
				'type':'password'
			}
		))

class CreateAccountForm(forms.Form):
	firstname = forms.CharField(label='First name', max_length=100, widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'First name',
				'autocomplete': 'off'
			}
		))
	lastname = forms.CharField(label='Last name', max_length=100, widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Last name',
				'autocomplete': 'off'
			}
		))
	username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Username',
				'autocomplete': 'off'
			}
		))
	password = forms.CharField(label='Password', max_length=100, widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Password',
				'type': 'password'
			}
		))

	email = forms.CharField(label='Email', max_length=100, widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Email',
				'type': 'password'
			}
		))

class CreateProjectForm(forms.Form):
	name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Name',
			'autocomplete': 'off'
		}
	))

	description = forms.CharField(label='Description', max_length=100, widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Description',
			'autocomplete': 'off'
		}
	))

	reward = forms.DecimalField(label='Reward($)', widget=forms.NumberInput(
		attrs={
			'class': 'form-control',
			'placeholder': '$0.00',
			'autocomplete': 'off'
		}
	))


	deadline = forms.DateField(label='Deadline', widget=forms.DateInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Deadline',
			'autocomplete': 'off'
		}
	))

class CreateTaskForm(forms.Form):
	name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Name',
			'autocomplete': 'off'
		}
	))

	description = forms.CharField(label='Description', max_length=200, widget=forms.TextInput(
		attrs={
			'class': 'form-control',
			'placeholder': 'Description',
			'autocomplete': 'off'
		}
	))

	reward = forms.DecimalField(label='Reward($)', widget=forms.NumberInput(
		attrs={
			'class': 'form-control',
			'placeholder': '$0.00',
			'autocomplete': 'off'
		}
	))

class EditProfileForm(UserChangeForm):

    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'
        )