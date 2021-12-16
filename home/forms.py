from django import forms

from departements.models import UserExtension
from departements.models import Etudiant

class ConnexionForm(forms.ModelForm):

    class Meta:
        model = UserExtension
        fields = ['username', 'password']



class InscriptionForm(forms.ModelForm):
    class Meta:

        model = UserExtension
        fields = ['username', 'last_name','email','password','password','departement' ,'appartient','date_de_naissance','lieu_de_naissance']
        widgets = {
            'password' : forms.PasswordInput ,
        }