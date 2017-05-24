from django.forms import ModelForm
from jedis.models import Candidate, Auth

class CandidateForm(ModelForm):
    class Meta:
        model = Candidate
        fields = '__all__'
        exclude = 'master',

class AuthForm(ModelForm):
    class Meta:
        model = Auth
        fields = '__all__'


