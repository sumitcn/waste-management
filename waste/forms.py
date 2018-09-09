from django import forms
from waste.models import complainform


class complain_form(forms.ModelForm):
	class Meta:
		model = complainform
		fields = ('complain','dustbin','subject')