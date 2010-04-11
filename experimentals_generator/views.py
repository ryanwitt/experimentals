from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from models import *

def experimental(request, id):
	return render_to_response(
		'experimentals_generator/experimental.html',
		RequestContext(request, {
			'object': get_object_or_404(Molecule, id=id),
		})
	)

