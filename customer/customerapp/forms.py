from django import forms
from .models import customer_details
 
 
# creating a form
class customer_detailsForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = customer_details
 
        # specify fields to be used
        fields = [
            "name",
            "location",
            "email",
            "phone_number",
            "status",
        ]