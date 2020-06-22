from django.shortcuts import get_object_or_404, render, redirect
from django.core.paginator import Paginator
from django.urls import reverse
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import auth
from django.contrib import messages
from pyfcm import FCMNotification
from accounts.models import User

# Create your views here.


def login_view(request):
    if request.user:
        return redirect('dashboard:home')
    template_name = 'registration/login.html'
    return render(request, template_name)


def login(request):
    template_name = 'registration/login.html'
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        messages.success(request, 'user successfully logged in.')
        return redirect(reverse('dashboard:home'))
    else:
        messages.error(request, 'Invalid username or password.')
        return render(request, template_name)


@login_required
def users(request):
    template_name = 'accounts/users.html'
    user_list = User.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(user_list, 10)
    qs = paginator.get_page(page)
    context = {
        'obj': qs
    }
    return render(request, template_name, context)


@login_required
def toggle_fees_status(request, pk):
    qs = get_object_or_404(User, pk=pk)
    print('users')
    print(qs.paid)
    if qs.paid == True:
        qs.paid = False
        qs.save()
        messages.warning(request, 'Status successfully deacivated.')
        return redirect(reverse('accounts:users'))
    else:
        qs.paid = True
        qs.save()
        messages.success(request, 'Status successfully activated.')
        return redirect(reverse('accounts:users'))
