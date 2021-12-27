from django.forms import ModelForm, TextInput, FileInput, Select, CheckboxInput, NumberInput, Textarea
from .models import Location, Rent


class LocationForm(ModelForm):
    class Meta:
        model = Location
        fields = (
            '__all__'
        )
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Enter location name'}),
            'parent': Select(attrs={'class': 'form-control', 'id': 'address'}),
            'is_active': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_active'}),
            'image': FileInput(attrs={'class': 'file-upload-default', 'id': 'imageUpload'}),
        }


class RentForm(ModelForm):
    class Meta:
        model = Rent
        fields = (
            '__all__'
        )
        widgets = {
            'name': TextInput(attrs={'class': 'form-control', 'id': 'name', 'placeholder': 'Enter location name'}),
            'bed_room': NumberInput(attrs={'class': 'form-control', 'id': 'bed_room'}),
            'bath_room': NumberInput(attrs={'class': 'form-control', 'id': 'bath_room'}),
            'price': TextInput(attrs={'class': 'form-control', 'id': 'price'}),
            'discount_price': TextInput(attrs={'class': 'form-control', 'id': 'discount_price'}),
            'rent_location': Select(attrs={'class': 'form-control', 'id': 'rent_location'}),
            'types': Select(attrs={'class': 'form-control', 'id': 'types'}),
            'is_available': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_available'}),
            'is_ac': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_ac'}),
            'is_wifi': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_wifi'}),
            'is_tv': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_tv'}),
            'breakfast': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'breakfast'}),
            'is_lunch': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_lunch'}),
            'is_dinner': CheckboxInput(attrs={'class': 'form-check-input', 'id': 'is_dinner'}),
            'descriptions': Textarea(
                attrs={'class': 'form-control', 'id': 'description', 'placeholder': 'Enter Description'}),
            'image': FileInput(attrs={'class': 'file', 'id': 'imageUpload'}),
            'gallery_image': FileInput(attrs={'class': 'imageUpload', 'id': 'imageUpload'}),
            'gallery_image2': FileInput(attrs={'class': 'imageUpload', 'id': 'imageUpload2'}),
            'gallery_image3': FileInput(attrs={'class': 'imageUpload', 'id': 'imageUpload3'}),
            'gallery_image4': FileInput(attrs={'class': 'imageUpload', 'id': 'imageUpload4'}),
        }