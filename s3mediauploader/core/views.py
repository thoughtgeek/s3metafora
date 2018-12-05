from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Document
from .forms import DocumentForm
from django.views.decorators.csrf import csrf_exempt
from django.http import QueryDict
from django.core.files.storage import default_storage

def upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()

    documents = Document.objects.all().order_by('-uploaded_at')[:5]
    return render(request, 'core/document_form.html', {
        'form': form,
        'documents':documents,
    })

# @csrf_exempt
# def filelist(request):
#     documents = Document.objects.all()
#     if request.method == 'POST':
#         print(str(request.POST.get('delFile')))
#     return render(request, 'core/filelist.html', {
#         'documents':documents,
#     })


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
    })
