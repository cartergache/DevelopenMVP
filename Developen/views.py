from django.shortcuts import render

from .forms import SignInForm, CreateAccountForm, CreateProjectForm, CreateTaskForm, EditProfileForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.http import Http404
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.urls import reverse

from Developen.models import Project, Task
from django.contrib.auth.models import User

def index(request):
	user = request.user
	userStatus = user.is_authenticated
	userName = user.get_username()

	if userStatus:
		userName = user.get_short_name()

	if user.is_authenticated:
		project_list = Project.objects.filter(user=user)
		context = {
			'project_list': project_list,
			'userName': userName
		}
		return render(request, 'developen/index.html', context)
	else:
		return redirect('/sign-in')


def sign_in(request):
	if request.method == 'POST':
		form = SignInForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)

				return redirect('/home')

			else:
				form = SignInForm()
				return render(request, 'developen/sign-in.html', {'form': form})
	else:
		form = SignInForm()
		return render(request, 'developen/sign-in.html', {'form': form})


def sign_out(request):
	logout(request)

	return redirect('/home')

def create_account(request):
	if request.method == 'POST':
		form = CreateAccountForm(request.POST)

		if form.is_valid():
			firstname = form.cleaned_data['firstname']
			lastname = form.cleaned_data['lastname']
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			email = form.cleaned_data['email']

			user = User.objects.create_user(username=username, email=email, password=password)

			user.first_name = firstname
			user.last_name = lastname

			user.save()

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)

				return redirect('/home')

			else:
				form = SignInForm()
				return render(request, '/sign-in.html', {'form': form})

	else:
		form = CreateAccountForm()

	return render(request, 'developen/create-account.html', {'form': form})

def delete_account(request):
	user = request.user

	user.delete()

	return redirect('/sign-in')

def create_project(request):
	if request.method == 'POST':
		form = CreateProjectForm(request.POST)

		if form.is_valid():
			name = form.cleaned_data['name']
			user = request.user
			description = form.cleaned_data['description']
			reward = form.cleaned_data['reward']
			deadline = form.cleaned_data['deadline']

			new_project = Project(name=name, user=user, description=description, reward=reward, deadline=deadline) # @TODO

			new_project.save()

			return redirect('/projects')
	else:
		form = CreateProjectForm()

	return render(request, 'developen/create-project.html', {'form': form})
	
def delete_project(request, project_id):
	try:
		project = Project.objects.get(pk=project_id)
	except Project.DoesNotExist:
		raise Http404("Project does not exist")
	
	project.delete()
	
	return redirect('/projects')

def project_detail(request, project_id):
	user = request.user
	userStatus = user.is_authenticated
	userName = user.get_username()

	if userStatus:
		userName = user.get_short_name()

	if user.is_authenticated:
		try:
			project = Project.objects.get(pk=project_id)
		except Project.DoesNotExist:
			raise Http404("Project does not exist")

		task_list = Task.objects.filter(project=project)

		context = {
			'project': project,
			'task_list': task_list,
			'userName': userName,
		}

		return render(request, 'developen/project-detail.html', context)
	else:
		return redirect('/sign-in')

def home(request):
	user = request.user
	userStatus = user.is_authenticated
	userName = user.get_username()

	if userStatus:
		userName = user.get_short_name()



	if request.method == 'POST':
		form = SignInForm(request.POST)

		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				userStatus = user.is_authenticated
				userName = user.get_short_name()

			else:
				form = SignInForm()
				return render(request, 'developen/sign-in.html', {'form': form})
	else:
		form = SignInForm()

	return render(request, 'developen/home.html', {'userStatus': userStatus, 'userName': userName, 'form': form})

def create_task(request, project_id):
	if request.method == 'POST':
		form = CreateTaskForm(request.POST)

		if form.is_valid():
			name = form.cleaned_data['name']
			project = Project.objects.get(pk=project_id)
			description = form.cleaned_data['description']
			reward = form.cleaned_data['reward']

			new_task = Task(name=name, project=project, reward=reward, description=description)

			new_task.save()

			return redirect('/' + str(project_id))

	else:
		form = CreateTaskForm()

	return render(request, 'developen/create-task.html', {'form': form})

def delete_task(request, project_id, task_id):
	user = request.user
	if user.is_authenticated:
		try:
			task = Task.objects.get(pk=task_id)
		except Task.DoesNotExist:
			raise Http404("Task does not exist")
		
		task.delete()
		
		return redirect('/' + str(project_id))
	else:
		return redirect('/sign-in')


def task_detail(request, project_id, task_id):
	user = request.user
	if user.is_authenticated:
		try:
			project = Project.objects.get(pk=project_id)
		except Project.DoesNotExist:
			raise Http404("Project does not exist")

		task = Task.objects.get(pk=task_id)

		context = {
			'project' : project,
			'task': task
		}

		return render(request, 'developen/task-detail.html', context)
	else:
		return redirect('/sign-in')



def my_account(request):
	user = request.user
	userStatus = user.is_authenticated
	userName = user.get_username()

	if userStatus:
		userName = user.get_short_name()

	if user.is_authenticated:
		first_name = user.first_name
		last_name = user.last_name
		full_name = first_name + " " + last_name
		date_joined = user.date_joined
		email = user.email
		password = user.password
		context = {
			'userStatus': userStatus,
			'userName': userName,
			'full_name': full_name,
			'first_name': first_name,
			'last_name': last_name,
			'date_joined': date_joined,
			'email': email,
			'password': password
		}

		return render(request, 'developen/my-account.html', context)
	else:
		return redirect('/sign-in')


def edit_my_account(request):
	user = request.user
	userStatus = user.is_authenticated
	userName = user.get_username()

	if userStatus:
		userName = user.get_short_name()

	if request.method == 'POST':
		form = EditProfileForm(request.POST, instance=request.user)

		if form.is_valid():
			form.save()
			return redirect('/my-account')
	elif userStatus:
		form = EditProfileForm(instance=request.user)

		context = {
			'form': form,
			'userStatus': userStatus,
			'userName': userName
		}

		return render(request, 'developen/edit-profile.html', context)
	else:
		redirect('/sign-in')


def change_password(request):
	user = request.user
	userStatus = user.is_authenticated
	userName = user.get_username()

	if userStatus:
		userName = user.get_short_name()


	if request.method == 'POST':
		form = PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect('/my-account')
		else:
			return redirect('/change-password')
	else:
		form = PasswordChangeForm(user=request.user)

		context = {
			'form': form,
			'userStatus': userStatus,
			'userName': userName
		}
		return render(request, 'developen/change_password.html', context)