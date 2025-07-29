from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as ans
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

def home(request):
    return render(request,"auth/home.html")
def about(request):
    return render(request,"auth/about.html")
def contact(request):
    return render(request,"auth/contact.html")
def redirect_to_users(request):
    return redirect('/admin/auth/user/')



# Create your views here.
def register_view(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            login(request,user)
            return redirect('predict')
    else:
        initial_data={'username':'','password1':'','password2':''}
        form=UserCreationForm(initial=initial_data)
    return render(request,'auth/register.html',{'form':form})

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('predict')
    else:
        form=AuthenticationForm()
    return render(request,'auth/login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')

def dashboard_view(request):
     return render(request,'auth/dashboard.html')

def admin_login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data={'username':'','Secret key':'',}
        form=UserCreationForm(initial=initial_data)
    return render(request,'auth/admin_login.html',{'form':form})

def predict(request):
    return render(request,"auth/prediction.html")

def result(request):
        data = pd.read_csv(r"D:\archive\USA_Housing.csv")
        data = data.drop(["Address"], axis=1)
        X = data.drop('Price', axis=1)
        Y = data['Price']
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=.30)
        model = LinearRegression()
        model.fit(X_train, Y_train)

        var1 = float(request.GET['n1'])
        var2 = float(request.GET['n2'])
        var3 = float(request.GET['n3'])
        var4 = float(request.GET['n4'])
        var5 = float(request.GET['n5'])

        pred = model.predict(np.array([var1, var2, var3, var4, var5]).reshape(1, -1))
        pred = round(pred[0])

        price = "The predicted price is $" + str(pred)

        return render(request, "auth/prediction.html", {"result2": price})


