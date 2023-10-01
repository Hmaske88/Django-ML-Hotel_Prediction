from django.shortcuts import render
import joblib
from predict.models import DataBase
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from csv import writer

# Create your views here.
def index(request):
    if request.method == 'POST':
        # Get data from the request
        location = request.POST.get('location')
        rent = request.POST.get('rent')
        stars = request.POST.get('stars')
        food = request.POST.get('food')
        foodType = request.POST.get('foodType')
        discount = request.POST.get('discount')
        # Make predictions using your ML model
        prediction = getPrediction(location, rent, stars, food, foodType, discount)
        return render(request,"index.html",{"result":prediction})
    
    return render(request, "index.html")

def getPrediction(location, rent, stars, food, foodType, discount):
    naive_bayes=joblib.load("naive_bayes.sav")

    d={0:'The Cafe Terrace',1:'The Cherry Blossom',2:'The Cutting Board',3:'The Diamond',4:'The Golden Fork',5:'The Green Plate',6:'The Chef’s Table',7:'The Bell Tower',8:'The Brick Oven'}

    List=[location,rent,stars,food,foodType,discount]
    with open('input.csv', 'a') as f_object:
        writer_object = writer(f_object)
        writer_object.writerow(List)
        f_object.close()

    new_data=pd.read_csv("input.csv")
    new2=new_data.copy()
    le=LabelEncoder()
    new2['area']=le.fit_transform(new2['area'])
    new2['rent']=le.fit_transform(new2['rent'])
    new2['stars']=le.fit_transform(new2['stars'])
    new2['food']=le.fit_transform(new2['food'])
    new2['food type']=le.fit_transform(new2['food type'])
    new2['discount']=le.fit_transform(new2['discount'])
    prediction = naive_bayes.predict(new2.tail(1))
    new_data = new_data.iloc[:-1]
    new_data.to_csv('input.csv', index=False)

    return d[prediction[0]]