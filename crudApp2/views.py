from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from Experiment2.settings import LOGIN_URL
from .models import Book
from .forms import BookCreate
from django.http import HttpResponse
#DataFlair
@login_required(login_url=LOGIN_URL)
def index(request):
    shelf = Book.objects.all()
    return render(request, 'crudApp2/library.html', {'shelf': shelf})
@login_required(login_url=LOGIN_URL)
def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'crudApp2/Upload_form.html', {'upload_form':upload})
@login_required(login_url=LOGIN_URL)
def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookCreate(request.POST or None, request.FILES or None ,instance = book_sel )
    print(book_form)
    # book_form.picture =request.FILES
    if book_form.is_valid():
        # book_form=BookCreate(request.POST or None)
        book_form.save()
        return redirect('index')
    return render(request, 'crudApp2/Upload_form.html', {'upload_form':book_form})
@login_required(login_url=LOGIN_URL)
def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')