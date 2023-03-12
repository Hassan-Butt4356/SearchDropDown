from .models import Post
# from dal import autocomplete
from django import forms
# from dal.autocomplete.
class PostCreateForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'

        status = forms.ChoiceField(choices=Post.STATUS_CHOICES, widget=forms.Select(attrs={'class': 'ch'}))
        # widgets = {
        #     'status': autocomplete.Select(
        #         # url=reverse('create'),
        #         # attrs={
        #         #     'data-placeholder': 'Type to search...',
        #         #     'data-minimum-input-length': 2,
        #         # },
        #         # model=Post,
        #     )
        # }
