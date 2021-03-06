from django.shortcuts import render, redirect
from django.views.generic import ListView, View, FormView
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate, logout

class LoginController(View):

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        password = request.POST['password']

        try:
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                request.session['user_id'] = user.id
                return HttpResponseRedirect(reverse('tasker:task-user'))

            else:
                return HttpResponse("wrong credentials, please try again <a href='/'>go back</a>")

        except:
            raise HttpResponseServerError()


class RegisterController(View):

    def post(self, request, *args, **kwargs):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.create_user(username = username, email = email, password = password)
            user.save()
            get_login = authenticate(username = username, password = password)

            if get_login is not None:
                login(request, get_login)
                request.session['user_id'] = user.id

        except:
            raise HttpResponseServerError()

        else:
            return HttpResponseRedirect(reverse('tasker:task-user'))
