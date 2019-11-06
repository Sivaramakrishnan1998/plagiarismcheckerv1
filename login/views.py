from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render
from login.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,login,authenticate
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.template.loader import render_to_string
from .forms import RegistrationForm,InstituteRegistrationForm
from checker.models import Credits,Institution

@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],email=form.cleaned_data['email'])

            #send_mail(subject,message,from_email,to_list,fail_silently=True)
            user = User.objects.get(pk = user.id)
            user.institution.flag = 0
            user.credits.credits = 1000
            user.save()
            
            # credits = Credits(user =user['User'],credits = 1000)
            subject = 'Hello from QUIZZY'
            message = 'Hi there, ' + request.POST['username'] +'\nThanks for registering with us. Please visit our site to take a test now (quizzy.pythonanywhere.com)'
            from_email = settings.EMAIL_HOST_USER
            to_list = [request.POST['email']]
            send_mail(subject,message,from_email,to_list,fail_silently=True)
            return render(request,'login/success.html',{'user':user})
    else:
        form = RegistrationForm()
    # variables = RequestContext(request, {'form': form})
    return render(request,'login/register1.html',{'form':form})

def register_success(request):
    return render(request,'login/success.html')

@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')

@login_required
def home(request):
    return render_to_response('home.html',{ 'user': request.user })

@csrf_protect
def user_login_and_register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard')

    if request.method == 'POST' and 'loginbutton' in request.POST:
        username = request.POST['username'] 
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                # return render(request,'base.html',{'user':user})
                return HttpResponseRedirect('/dashboard')
            else:
                return HttpResponse("This user account is disabled.")
        else:
            msg = 'Invalid credentials. Try again.'
        return render(request,'login/login1.html',{'msg':msg})
    elif request.method == 'POST' and 'registerbutton' in request.POST:
        try:
            user = User.objects.get(username__iexact=request.POST['username'])
            msg = 'User name already exists try different one'
            return render(request,'login/login1.html',{'msg':msg})
        except User.DoesNotExist:
            if(request.POST['password1']== '' or request.POST['password2']==''):
                msg = 'Password required'
                return render(request,'login/login1.html',{'msg':msg})
            if(request.POST['password1'] != request.POST['password2']):
                msg = 'Passwords do not match'
                return render(request,'login/login1.html',{'msg':msg})
            user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'],email=request.POST['email'])
            user.credits.credits = 1000
            user.save()
            return render(request,'login/success.html',{'user':user})
    return render(request,'login/login1.html')


@csrf_protect
def institution_login_and_register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard')
    print("institution")
    if request.method == 'POST' and 'loginbutton' in request.POST:
        username = request.POST['username'] 
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                # return render(request,'base.html',{'user':user})
                return HttpResponseRedirect('/dashboard')
            else:
                return HttpResponse("This user account is disabled.")
        else:
            msg = 'Invalid credentials. Try again.'
            return render(request,'login/institutionlogin.html',{'msg':msg})
    elif request.method == 'POST' and 'insregisterbutton' in request.POST:
        print("inside elif")
        try:
            user = User.objects.get(username__iexact=request.POST['username'])
            msg = 'User name already exists try different one'
            return render(request,'login/institutionlogin.html',{'msg':msg})
        except User.DoesNotExist:
            if(request.POST['password1']== '' or request.POST['password2']==''):
                msg = 'Password required'
                return render(request,'login/institutionlogin.html',{'msg':msg})
            if(request.POST['password1'] != request.POST['password2']):
                msg = 'Passwords do not match'
                return render(request,'login/institutionlogin.html',{'msg':msg})
            user = User.objects.create_user(username=request.POST['username'],password=request.POST['password1'],email=request.POST['email'])
            user.credits.credits = 5000
            user.save()
            user = User.objects.get(pk = user.id)
            print("inside institution")
            user.institution.name = request.POST['name']
            user.institution.mobile_no = request.POST['mobileno']
            user.institution.contact_person = request.POST['contactperson']
            user.institution.designation = request.POST['designation']
            user.institution.institution_name = request.POST['institute']
            user.save()
            user.institution.address = request.POST['address']
            user.save()
            return render(request,'login/success.html',{'user':user})
    return render(request,'login/institutionlogin.html')
