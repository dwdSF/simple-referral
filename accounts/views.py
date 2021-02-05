# from .utils import send_sms
from codes.forms import CodeForm
from django.contrib.auth import authenticate, get_user_model, login
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import UserLoginForm

User = get_user_model()


def login_view(request):
    ''' The function waits for the phone number data.
        Saves the user's pk in the session and passes control to verify view'''

    if request.user.is_authenticated:
        return redirect(reverse('profile-view'))

    form = UserLoginForm(request.POST or None)
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        user = authenticate(request, phone_number=phone_number)

        if user is not None:
            request.session['pk'] = user.pk
            return redirect(reverse('verify-view'))

        if form.is_valid():
            user = form.save()
            request.session['pk'] = user.pk
            return redirect(reverse('verify-view'))

    return render(request, 'login.html', {'form': form})


def verify_view(request):
    ''' The function processes the incoming redirect.
    Checks the pk in the session and sends the verification code.'''

    if request.user.is_authenticated:
        return redirect(reverse('profile-view'))
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    if pk:
        user = get_object_or_404(User, pk=pk)
        code = user.code
        user_code = f'{user.phone_number}: {code}'
        if not request.POST:
            # send_sms(user_code, user.phone_number)  # Twilio part here
            print(user_code)
        if form.is_valid():
            num = form.cleaned_data.get('number')

            if str(code) == num:
                code.save()
                login(request, user)
                return redirect(reverse('profile-view'))

            return redirect(reverse('login-view'))

    return render(request, 'verify.html', {'form': form})


def page_not_found(request, exception):
    context = {
        'path': request.path
    }
    return render(request, 'misc/404.html', context, status=404)


def server_error(request):
    return render(request, 'misc/500.html', status=500)
