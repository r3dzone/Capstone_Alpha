from django.http import request
from django.shortcuts import redirect, render
from django.views import View
from django.http import HttpResponse
import json

# Dashboard
class DashboardView(View):
    def get(self, request):
        return render(request, 'index.html')

# Dashboard
class MainaddView(View):
        def get(self, request):
            return render(request, 'mainadd.html')


# Create your views here.
