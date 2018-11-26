from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Document
from .forms import DocumentForm

def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()

    documents = Document.objects.all()
    return render(request, 'core/document_form.html', {
        'form': form,
        'documents':documents,
    })
