from django.forms import ModelForm
from tracecards.models import Tracecard

class TracecardForm(ModelForm):
	
	class Meta:
		model = Tracecard
		exclude = ('creator', 'offer', 'order', 'status')