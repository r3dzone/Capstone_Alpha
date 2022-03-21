
from django.http import request
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
import json

# Dashboard
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


