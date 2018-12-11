import random
from django.http import QueryDict
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Document
from .forms import DocumentForm, UserRegistrationForm


def upload(request):
    if request.method == 'GET' and not request.user.is_authenticated:
            auth_token = request.GET.get('auth_token')
            print(auth_token)
            user = authenticate(request, username=auth_token,
                                password=auth_token)
            if user is not None:
                login(request, user)
            else:
                return HttpResponse('Authentication Required')

    if request.user.is_authenticated:
        if request.method == 'POST':
            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                documentform_unsaved  = form.save(commit=False)
                documentform_unsaved.uploader = request.user
                documentform_unsaved.save()
                return redirect('home')
        else:
            form = DocumentForm()

        documents = Document.objects.all().order_by('-uploaded_at')[:5]
        return render(request, 'core/document_form.html', {
            'form': form,
            'documents':documents,
            'user_email':request.user.email,
        })


@login_required
@csrf_exempt
def filelist(request):
    documents = Document.objects.all()
    if request.method == 'DELETE':
        delFile = str(QueryDict(request.body).get('delFile'))
        try:
            delFile = str(QueryDict(request.body).get('delFile'))
            Document.objects.filter(upload=delFile).delete()
            default_storage.delete(delFile)
            print('File deleted successfully!')
        except:
            print('Error in file deletion!')
    return render(request, 'core/filelist.html', {
        'documents':documents,
        'user_email':request.user.email,
    })


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            email =  userObj['email']
            auth_token = token_generator()
            while User.objects.filter(username=auth_token).exists():
                auth_token = token_generator()
            if not User.objects.filter(email=email).exists():
                User.objects.create_user(auth_token, email, auth_token)
                return render(request, 'core/register_success.html',
                              {'auth_token' : auth_token})
            else:
                raise forms.ValidationError('Looks like a user with that email already exists')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {
        'form' : form,
        'user_email':request.user.email,
    })


def log_out(request):
    logout(request)
    return HttpResponse('Logged out successfully!')

def token_generator():
    chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijnopqrstuvwxyz1234567890'
    auth_token= ''.join((random.choice(chars)) for x in range(10))
    return(auth_token)
