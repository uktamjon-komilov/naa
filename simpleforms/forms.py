from django import forms

from .models import Filial, News, Director


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        exclude = ["views"]

    def __init__(self, *args, **kwargs):
        super(NewsForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs["class"] = "form-control"
        
    
class DirectorForm(forms.ModelForm):
    class Meta:
        model = Director
        fields = ["fullname", "experience"]


class FilialForm(forms.ModelForm):
    established_at = forms.DateTimeField(input_formats=["%d.%m.%Y %H:%M"])

    class Meta:
        model = Filial
        fields = ["title", "established_at"]