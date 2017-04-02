from django import forms
from workers.models import JobPosition

class JobPositionForm(forms.ModelForm):
    class Meta:
        model = JobPosition
        fields = [
            'name',
            'created',
        ]