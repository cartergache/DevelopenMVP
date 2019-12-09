from django.urls import path


from . import views

urlpatterns = [
    path('projects/', views.index, name='index'),
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-out/', views.sign_out, name='sign-out'),
    path('my-account/', views.my_account, name='my-account'),
    path('my-account/edit', views.edit_my_account, name='edit-my-account'),
    path('my-account/change-password', views.change_password, name='change-password'),
    path('create-account/', views.create_account, name='create-account'),
    path('delete-account/', views.delete_account, name='delete-account'),
    path('create/', views.create_project, name='create-project'),
    path('<int:project_id>/delete/', views.delete_project, name='delete-project'),
    path('<int:project_id>/detail/', views.project_detail, name='project-detail'),
    path('home/', views.home, name='home'),
    path('<int:project_id>/', views.project_detail, name='project-detail'),
    path('<int:project_id>/tasks/create/', views.create_task, name='create-task'),
    path('<int:project_id>/tasks/<int:task_id>/delete/', views.delete_task, name='delete-task'), 
    path('<int:project_id>/tasks/<int:task_id>/', views.task_detail, name='task-detail')
]
