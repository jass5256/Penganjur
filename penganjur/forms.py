from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions
from django.db import models
from .models import Aktiviti

class Aktivitiform(forms.ModelForm):
	class Meta:
		model=Aktiviti
		fields=('tajuk','tempat','penceramah','hadpeserta',)