from django import forms
from recipes.models import Recipes, Comment


class RecipesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, field) in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Recipes
        exclude = ('user','timestamp',)
        widgets = {
            'image_url': forms.TextInput(
                attrs={
                    'id': 'img_input',
                }
            )
        }
# class RecipesForm(forms.ModelForm):
#     class Meta:
#         model = Recipes
#         exclude = ("user",)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.Textarea(
                attrs= {
                    'class': 'form-control rounded-2',
                    'is_required': True,
                },
            ),
        }


