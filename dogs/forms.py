import datetime

from django import forms

from dogs.models import Dog, DogParent
from users.forms import StyleFromMixin


class DogForm(StyleFromMixin,forms.ModelForm):
    class Meta:
        model = Dog
        exclude = ('owner',)

    def clean_birth_date(self):
        cleaned_data = self.cleaned_data['birth_date']
        now_year = datetime.datetime.now().year
        if now_year - cleaned_data.year >35:
            raise  forms.ValidationError('Cобака должна быть моложе 35 лет')
        return cleaned_data



class DogParentForm(StyleFromMixin,forms.ModelForm):
    class Meta:
        model = DogParent
        fields = '__all__'