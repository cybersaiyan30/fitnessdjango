from django.shortcuts import render
from . models import SubsciptionTable,Store,Diet
from .forms import UserProfileInfoForm,UserForm

from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout



#import logging

#logger = logging.getLogger(__name__)

def home(request):
    return render(request, 'subscribe/home.html')

def subscribe(request):
    if not request.POST['email_sub']:
        #logger.error("HERE")
        return render(request, 'subscribe/home.html',{"err_msg":" e-mail is mandatory "})
    email=request.POST['email_sub']
    subuser = SubsciptionTable.objects.all()
    flag=0
    for user in subuser:
        if email == user.email:
            flag=1
            break
    if (flag == 1):
        return render(request, 'subscribe/home.html',{"msg":"You are already subscribed to us "})
    else:
        new_user=SubsciptionTable()
        new_user.email=email
        new_user.save()
        return render(request, 'subscribe/home.html', {"msg": "Thank you for subscribing. We'll keep you updated "})

def store(request):
    product_list=Store.objects.all()
    return render(request,'subscribe/store.html',{'product_list':product_list})

def diet(request):
    diet_list=Diet.objects.all()
    return render(request,'subscribe/diet.html',{'diet_list':diet_list})

def men(request):
    return render(request,'subscribe/men.html')


def register(request):
    registered = False

    if request.method == "POST":

        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()

            registered = True

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request, 'subscribe/registration.html',
                  {'user_form': user_form,
                   'profile_form': profile_form,
                   'registered': registered})


@login_required
def user_logout(request):
    logout(request)
    return render(request, 'subscribe/home.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return render(request, 'subscribe/home.html', {'user': user})
            else:
                return HttpResponse("ACCOUNT NOT ACTIVE")
        else:
            print("Someone tried to login and failed")
            print("username : {} password:{}".format(username, password))
            return HttpResponse("Invalid login details provided")

    else:
        return render(request, 'subscribe/login.html')
























