
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf

# Create your views here.

from .forms import SignUpForm

def home(request):
    
    form = SignUpForm(request.POST or None)
    
    if form.is_valid():
        save_it = form.save(commit=False)
        save_it.save()
        #send_mail(ubject, message, from_email, to_list, fail_silently=True)
        subject = 'Thank you for signing up to Smart Labels Central'
        message = 'Welcome ' + save_it.first_name + ' to smart labels central website where you can buy smart labels and track them in realtime'
        from_email = settings.EMAIL_HOST_USER
        to_list = [save_it.email, settings.EMAIL_HOST_USER]
        
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        messages.success(request, 'Thank you for joining, we will be in touch')
        return HttpResponseRedirect('/thank-you/')                   
    return render_to_response("signup.html", locals(), context_instance=RequestContext(request))

def thankyou(request):
    return render_to_response("thankyou.html", locals(), context_instance=RequestContext(request))

def testmap(request):
    return render_to_response("testmap.html", locals(), context_instance=RequestContext(request))

def learnmore(request):
    return render_to_response("learnmore.html", locals(), context_instance=RequestContext(request))

def login(request):
    c={}
    c.update(csrf(request))
    return render_to_response('login.html', c)


    

def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password=password)
    
    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/loggedin')
    else:
        return HttpResponseRedirect('/invalid')
    
def loggedin(request):
    return render_to_response('loggedin.html', {'full_name', request.user.username})

def invalid_login(request):
    return render_to_response('invalid_login.html')

def logout(request):
    auth.logout(request)
    return render_to_response('logout.html')
