from django.shortcuts import render,redirect,HttpResponse
from .forms import RegisterForm,LoginForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Parameters
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def Home(request):
    posts=Parameters.objects.all()
    return render(request,'HealthcareApp/Homepage.html',{'posts':posts})
def Register(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request,'HealthcareApp/Registerpage.html',{"form":form})

def Logins(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            user=authenticate(request,username=info['username'],password=info['password'])
            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('home')
                else:
                    return HttpResponse("disableAccount")
            else:
                return HttpResponse("invalid login")
    else:
        form = LoginForm()
    return render(request, 'HealthcareApp/Loginpage.html', {"form": form})
@login_required()
def Logout(request):
    logout(request)
    return redirect('home')
def Result(request):
    query=request.GET['query']
    posts = Parameters.objects.filter(emp_name__icontains=query)
    data = pd.read_csv('HealthcareApp/Employees_detail_csv2.csv')
    x = data.drop('result', axis=1)
    y = data['result']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30)
    model = LogisticRegression()
    model.fit(x_train, y_train)
    for i in posts:
        a = float(i.body_temp)
        b = float(i.blood_pres)
        c = float(i.glucose)
        d = float(i.heart_rate)
        e = float(i.oxygen_satu)
    pred = model.predict([[a, b, c, d, e]])
    res = ''
    if pred == [1]:
        res = 'positive'
    else:
        res = 'negative'
    return render(request, 'HealthcareApp/Resultpage.html',{'posts':posts,'res':res})
def Data(request):
    posts=Parameters.objects.all()
    return render(request, 'HealthcareApp/Datapage.html', {'posts': posts})
def Delete(request,pk):
    items=Parameters.objects.get(id=pk)
    if request.method == 'POST':
        items.delete()
        return redirect("data")
    context={
        "items": items
    }
    return render(request,'HealthcareApp/delete.html',context)