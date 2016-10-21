from django.template.loader import get_template
from django.template import Template, Context
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response, render
import postgresql
from list.models import *

def list(request):
	return render(request, 'list.html', {})

	