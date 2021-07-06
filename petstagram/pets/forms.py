from django import forms

from petstagram.core.forms import BootstrapFormMixin    #прави формата джиджана буутстрапска
from petstagram.pets.models import Pet


class PetForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Pet
        fields = '__all__'


class EditPetForm(PetForm):                  #ако изглежда същата можем да я наследим без проблем
    class Meta:
        model = Pet
        fields = '__all__'
        widgets ={
            'type': forms.TextInput(        #полето тип го правим неактивно, за да не можем да го сменяме
                attrs={
                    'readonly': 'readonly'
                }
            )
        }
