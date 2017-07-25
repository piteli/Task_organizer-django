from django.conf.urls import url, include
from .views import TaskIndexView, TaskDelete
from .views import TaskCreate, TaskUpdate
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^user/$',login_required(TaskIndexView.as_view()), name='task-user'),
    url(r'^delete-task/(?P<task_id>\d+)$', login_required(TaskDelete.as_view()), name='task-delete'),
    url(r'^add-task/$', login_required(TaskCreate.as_view()), name='task-add'),
    url(r'^edit-task/(?P<pk>\d+)$', login_required(TaskUpdate.as_view()), name='task-edit'),
]
