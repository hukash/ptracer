from django.shortcuts import render_to_response
from tracecards.models import Tracecard
from django.template import RequestContext
from tracecards.forms import TracecardForm
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

def all(request):
	all_tracecards = Tracecard.objects.all() #.order_by('deadline')
	context = {
		'all_tracecards': all_tracecards,
	}
	return render_to_response(
		'tracecards/all.html',
		context,
		context_instance = RequestContext(request),
	)

def create(request):
	form = TracecardForm(request.POST or None)
	if form.is_valid():
		tracecard = form.save(commit=False)
		tracecard.creator = request.user
		tracecard.status = "in_process"
		tracecard.save()
		request.user.message_set.create(message="Tracecard was created.")
		#eric uses a if 'next' in RequestPost, why?
		return HttpResponseRedirect(reverse('tracecards_all'))
	else:
		#need to understand how render_to_response works
		return render_to_response(
			'tracecards/create.html',
			{'form': form},
			context_instance = RequestContext(request)
		)
		