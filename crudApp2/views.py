from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.utils.html import strip_tags

from Experiment2.settings import LOGIN_URL
from .models import Book
from .forms import BookCreate , SignUpForm
from django.http import HttpResponse

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from .tokens import account_activation_token

from django.contrib.auth import login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your MySite Account'
            message = render_to_string('crudApp2/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            #user.email_user(subject,"", html_message=message)
            email_from = 'daksh.batra0@gmail.com'
            recipient_list = str(form['email'].value())
            print(recipient_list)
            connection = [
                'daksh.batra0@gmail.com',
                'Him@199b',
                False,
            ]
            send_mail(subject, strip_tags(message), email_from, [recipient_list], connection)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'crudApp2/signup.html', {'form': form})

def account_activation_sent(request):
    return render(request, 'crudApp2/account_activation_sent.html')

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('login')
    else:
        return render(request, 'crudApp2/account_activation_invalid.html')

#DataFlair
@login_required(login_url=LOGIN_URL)
def index(request):
    shelf = Book.objects.all()
    print(request.user)
    username=request.user.get_username()
    return render(request, 'crudApp2/library.html', {'shelf': shelf,'name':username})

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
        return render(request, 'crudApp2/upload_form.html', {'upload_form':upload})

@login_required(login_url=LOGIN_URL)
def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookCreate(request.POST or None, request.FILES or None ,instance = book_sel )
    if book_form.is_valid():
        date = book_form.cleaned_data['release_date']
        book_form.save()
        return redirect('index',{'date':date})
    return render(request, 'crudApp2/upload_form.html', {'upload_form':book_form})


@login_required(login_url=LOGIN_URL)
def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')

# #def signup_view(request):
#  #   form = UserCreationForm(request.POST)
#  #    if form.is_valid():
#         form.save()
#         print(form.cleaned_data)
#         username = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password1')
#         user = authenticate(username=username, password=password)
#         print(user)
#         login(request,user)
#         print(request.session)
#         return redirect('login')
#     return render(request, 'crudApp2/signup.html', {'form': form})