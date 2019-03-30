from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import user_SignUpForm,DocumentForm
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.core.mail import EmailMessage
from .models import Document
def user_register(request):
    if request.method == 'POST':
        form = user_SignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')

        else:
            return render(request, 'part1/register.html', {'form': form})
    else:
        form =user_SignUpForm()
        return render(request, 'part1/register.html', {'form': form})


def  user_login(request):
    si=""
    if request.user.is_authenticated:
        return redirect('upload')

    elif request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if request.user.is_authenticated:
                return redirect('upload')
            else:
                s="incorret password"
                return render(request, 'part1/login.html', {'form': form,'si':s})
        else:
            return render(request, 'part1/login.html', {'form': form,'si':si})


    else:
        form = AuthenticationForm()
        return render(request, 'part1/login.html', {'form': form})

def pagelogout(request):
        logout(request)
        return redirect('http://127.0.0.1:8000/')

def upload(request):
  if request.user.is_authenticated:
    s = request.user.username
    a = Document.objects.filter(userid=s)
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print(a, "upload")
            form.save()
            return render(request, 'part1/upload.html', {'form': form, 's': s, 'l': a})
        else:
            return render(request, 'part1/upload.html', {'form': form, 's': s, 'l': a})
    else:
        form = DocumentForm()

        return render(request, 'part1/upload.html', {'form': form,'s':s,'l':a})
  else:
    return HttpResponse("<h1>please login to continue</h1>")


def files(request):
  if request.user.is_authenticated:
    s = request.user.username
    a = Document.objects.filter(userid=s)
    '''if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'part1/files.html', {'form': form, 's': s, 'l': a})
        else:
            return render(request, 'part1/files.html', {'form': form, 's': s, 'l': a})'''

    return render(request, 'part1/files.html', {'l':a})
  else:
    return HttpResponse("<h1>please login to continue</h1>")

def ViewProfile(request):
  if request.user.is_authenticated:
    s = request.user.username
    a = Document.objects.filter(userid=s)
    present=0
    if request.method == 'POST':
         s=request.POST.get('userid1')
         if(User.objects.filter(username=s).exists()):
             present=1
             c=User.objects.filter(username=s)
             return render(request, 'part1/profile.html', {'present': present,'c':c[0]})

         else:
            present=0
            return render(request, 'part1/profile.html', {'present':present,'d': "user not found.Enter correct username"})
    else:

        return render(request, 'part1/profile.html', {'present':present})
  else:
    return HttpResponse("<h1>please login to continue</h1>")


def sendto(request,usr,fil):
  if request.user.is_authenticated:
    s1 = request.user.username
    msg=""
    if request.method == 'POST':
         s=request.POST.get('userid1')
         s1 = request.user.username
         if(usr!=s1):
             return redirect('upload')
         z=Document.objects.filter(userid=s1,name=fil)
         print("hiiiiiii",len(z),s)
         z=z[0]
         if(User.objects.filter(username=s).exists()):
             f=Document()
             f.userid=s
             f.description=z.description
             f.document=z.document
             f.uploaded_at=z.uploaded_at
             f.name=z.name
             f.save()
             print(f.description,f.name)
             msg = "successful"
             return render(request, 'part1/usr1.html', {'msg': msg})
         else:
             msg = "*wrong username"
             return render(request, 'part1/usr1.html', {'msg': msg})



    else:

        return render(request, 'part1/usr1.html',{'msg':msg})
  else:
    return HttpResponse("<h1>please login to continue</h1>")



def contact(request):
  if request.user.is_authenticated:
        return render(request,'part1/about.html')

  else:
    return HttpResponse("<h1>please login to continue</h1>")
