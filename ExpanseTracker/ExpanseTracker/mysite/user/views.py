from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from .form import Registration
from django.contrib.auth.forms import AuthenticationForm
def register(request):
    print(request.user)
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=Registration(request.POST)
            if form.is_valid():
                form.save()
                return redirect('user:login')
        else:
            form=Registration()
        return render(request,'user/Signup.html',{'form':form})
    else:
        return redirect("myapp:index")



def LoginView(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
                form = AuthenticationForm(request, data=request.POST)
                if form.is_valid():
                    username = form.cleaned_data.get('username')
                    password = form.cleaned_data.get('password')
                    user = authenticate(request, username=username, password=password)
                    if user is not None:
                        login(request, user)
                        return redirect("myapp:dashbord")
        else:
            form = AuthenticationForm()

        return render(request, 'user/login.html', {'form': form})
    return redirect('myapp:index')
def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('user:login')
    else:
        return redirect('user:login')
