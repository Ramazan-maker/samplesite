from django import forms
from django.core import validators

from .models import Img


# class ImgForm(forms.ModelForm):
#     img = forms.ImageField(label='Изображение',
#                            validators=[
#                                validators.FileExtensionValidator(
#                                    allowed_extensions=('gif', 'jpg', 'png'))],
#                            error_messages={
#                                'invalid_extension': 'Этот формат не поддерживается'})
#     desc = forms.CharField(label='Описание',
#                            widget=forms.widgets.Textarea())
#
#     class Meta:
#         model = Img
#         fields = '__all__'

class ImgForm(forms.ModelForm):
    img = forms.ImageField(label='Изображение',
                           validators=[
                               validators.FileExtensionValidator(
                                   allowed_extensions=('gif', 'jpg', 'png'))],
                           error_messages={
                               'invalid_extension': 'Этот формат не поддерживается'})
    desc = forms.CharField(label='Описание',
                           widget=forms.widgets.Textarea())
    xlsx_file = forms.FileField(label='Файл XLSX', required=False)
    pdf_file = forms.FileField(label='Файл PDF', required=False)

    class Meta:
        model = Img
        fields = '__all__'
