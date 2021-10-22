from django import forms
from django.utils.translation import gettext_lazy as _
from book_manager.views import Book, Author

class CreateBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30)
    date_of_birth = forms.DateField( required=True)
    date_of_death = forms.DateField( required=False)

    def __init__(self, *args, **kwargs):
        super(CreateBook, self).__init__(*args, **kwargs)
        self.fields['author'].required = False

    def clean(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        date_of_birth = self.cleaned_data.get('date_of_birth')
        date_of_death = self.cleaned_data.get('date_of_death')


        obj, created = Author.objects.get_or_create(first_name=first_name, last_name=last_name, date_of_birth=date_of_birth, date_of_death=date_of_death)
        self.cleaned_data['author'] = obj

        return super(CreateBook, self).clean()

class CreateAuthor(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'
        help_texts = {
            'first_name': _('Required'),
            'last_name': _('Required'),
            'date_of_birth': _('Required')
        }