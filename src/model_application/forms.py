from django import forms
from .utils import predict_model

class HouseApplicationForm(forms.Form):
    bedrooms = forms.IntegerField(label='bedrooms',help_text="enter number for the amount of bedrooms")
    bathrooms = forms.IntegerField(label='bathrooms',help_text="enter number for the amount of bathrooms")
    sqft_living = forms.IntegerField(label='sqft_living',help_text="enter the square feet for living room")
    sqft_lot = forms.IntegerField(label='sqft_lot',help_text="enter the lot size in square feet")
    floors = forms.IntegerField(label='floors',help_text="enter the number of floors")
    water_front = forms.IntegerField(label='water_front',help_text="enter number for the amount of water fronts")
    condition = forms.IntegerField(label='condition',help_text="enter number for the condition")
    view = forms.IntegerField(label='view',help_text="enter number for the amount of view")
    sqft_above = forms.IntegerField(label='sqft_above',help_text="enter number for square feet above")
    sqft_basement = forms.IntegerField(label='sqft_basement',help_text="enter number for square feet basement")
    yr_build = forms.IntegerField(label='yr_build',help_text="enter number for years built")
    yr_renovated = forms.IntegerField(label='yr_renovated',help_text="enter number for the amount of years since renovation")
    street = forms.CharField(label='street',help_text="enter street address",max_length=150)
    city = forms.CharField(label='city',max_length=150,help_text="enter city name")
    state_zip = forms.CharField(label='state_zip',max_length=150,help_text="enter state zip address")
    country = forms.CharField(label='country',max_length=150,help_text="enter country of home")



    