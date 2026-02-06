from django import forms

from pets.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'date_of_birth', 'personal_photo']

        labels = {
            'name': 'Pet Name',
            'date_of_birth': 'Date of Birth',
            'personal_photo': 'Image URL',
        }

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Enter pet name',
                }
            ),
            'date_of_birth': forms.DateInput(
                attrs={
                    'type': 'date',
                }
            ),
            'personal_photo': forms.URLInput(
                attrs={
                        'placeholder': 'Enter image URL',
                }
            ),
        }


class PetDeleteForm(PetForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            # field.widget.attrs['disabled'] = True
            # field.widget.attrs['readonly'] = True
            field.disabled = True
            field.readonly = True

    # def save(self, commit=True):
    #     if commit:
    #         self.instance.delete()
    #     return self.instance