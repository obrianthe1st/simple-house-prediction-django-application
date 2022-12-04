from django.shortcuts import render,redirect
from .forms import HouseApplicationForm
from .utils import predict_model

from django.http import HttpResponse


# Create your views here.
def homeView(request):
    context = {}
    if request.method == "POST":
        form = HouseApplicationForm(request.POST or None)
        if form.is_valid():
            bedrooms = form.cleaned_data['bedrooms']
            bathrooms = form.cleaned_data['bathrooms']
            sqft_living = form.cleaned_data['sqft_living']
            sqft_lot = form.cleaned_data['sqft_lot']
            floors = form.cleaned_data['floors']
            water_front = form.cleaned_data['water_front']
            view = form.cleaned_data['view']
            condition = form.cleaned_data['condition']
            sqft_above = form.cleaned_data['sqft_above']
            sqft_basement = form.cleaned_data['sqft_basement']
            yr_build = form.cleaned_data['yr_build']
            yr_renovated = form.cleaned_data['yr_renovated']
            street = form.cleaned_data['street']
            city = form.cleaned_data['city']
            state_zip = form.cleaned_data['state_zip']
            country = form.cleaned_data['country']

            prediction = predict_model(bedrooms,bathrooms,sqft_living,sqft_lot,floors,water_front,view,condition,sqft_above,sqft_basement,yr_build,yr_renovated,addr="../Model/regression_model.sav")
            return render(request,'results.html',context={"model_result":round(prediction[0],2)})    
        else:
            return("not working")
    else:
        print("not working")
        form = HouseApplicationForm()
    return render(request,'index.html',{"form":form})
