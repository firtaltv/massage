from django import forms


class ProfilePhotoForm(forms.Form):
    profile_photo_field = forms.ImageField()