from django.shortcuts import render
from django.views.generic import ListView, View, FormView
from .models import Task
from .forms import AddTaskForm, UpdateTaskForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
import datetime
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

class TaskIndexView(ListView):
    template_name="task.html"
    context_object_name = "all_task"
    paginate_by = '5'

    def get_queryset(self):
        try:
            self.query_task = Task.objects.filter(user_id = self.request.session['user_id'])
            return self.query_task
        except:
            return "no data recorded"


class TaskDelete(View):

    def get(self, request, *args, **kwargs):
        try:
            get_id = Task.objects.get(pk = self.kwargs['task_id'])
            get_id.delete()

        except:
            return "Cannot Perform delete, Please try again"

        else:
            return HttpResponseRedirect(reverse('tasker:task-user'))

class TaskCreate(CreateView):
    model = Task
    form_class = AddTaskForm
    template_name_suffix = '_add_task'
    success_url = reverse_lazy('tasker:task-user')

    def get_initial(self):
        return {'dateCreated' : datetime.datetime.now().date(), 'user_id': self.request.session['user_id'] }


class TaskUpdate(UpdateView):
    model = Task
    form_class = UpdateTaskForm
    template_name_suffix = '_update_task'
    success_url = reverse_lazy('tasker:task-user')

    def get_initial(self):
        return {'dateUpdated' : datetime.datetime.now().date()}
