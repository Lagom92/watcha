from django import forms
from .models import Movie

class MovieForm(forms.Form):
    title = forms.CharField(max_length=100)
    title_en = forms.CharField(max_length=100)
    audience = forms.IntegerField()
    open_date = forms.DateField(
            widget=forms.widgets.DateInput(attrs={'type':'date'})
            )
    genre = forms.CharField(max_length=100)
    watch_grade = forms.CharField(max_length=100)
    score = forms.FloatField()
    poster_url = forms.CharField(max_length=100)
    description = forms.CharField(widget=forms.Textarea())
    
    
class MovieModelForm(forms.ModelForm):
    class Meta:
        # movie 모델을 선택하는거
        model = Movie
        # 전부 다 가져오는거, 부분선택도 가능함
        fields = '__all__'
        # open_date 를 약간 수정해주는거
        widgets = {
            'open_date':forms.DateInput(attrs={'type':'date'})
        }