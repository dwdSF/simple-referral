from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import ReferralForm
from .models import UserReferral

User = get_user_model()


@login_required
def profile_view(request):
    ''' Profile with data about the user and the people invited by them '''

    current_user = request.user
    referrals = current_user.referred.all()

    has_invite = False
    referrer = None
    if current_user.referrer.exists():
        has_invite = True
        referrer = current_user.referrer.get(referred=current_user)

    paginator = Paginator(referrals, 4)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'page': page,
        'paginator': paginator,
        'current_user': current_user,
        'has_invite': has_invite,
        'referrer': referrer,
        'form': ReferralForm
    }

    return render(request, 'profile.html', context)


@login_required
def invite_activation(request):
    ''' Invite code activation function with various checks '''

    form = ReferralForm(request.POST)
    invite_code = None
    if form.is_valid():
        invite_code = form.cleaned_data['invite_code']

    current_user = request.user
    try:
        referrer = User.objects.get(invite_code=invite_code)
    except User.DoesNotExist:
        return redirect(reverse('profile-view'))

    if current_user != referrer:
        UserReferral.objects.get_or_create(
            referred=current_user,
            referrer=referrer
        )
    return redirect(reverse('profile-view'))


@login_required
def referrer_profile(request, code):
    ''' Function for viewing the profile of any user '''

    try:
        user = User.objects.get(invite_code=code)
    except User.DoesNotExist:
        return redirect(reverse('profile-view'))
    print(user)

    if user == request.user:
        return redirect(reverse('profile-view'))

    referrals = user.referred.all()

    has_invite = False
    referrer = None
    if user.referrer.exists():
        has_invite = True
        referrer = user.referrer.get(referred=user)

    paginator = Paginator(referrals, 4)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)

    context = {
        'page': page,
        'paginator': paginator,
        'current_user': user,
        'has_invite': has_invite,
        'referrer': referrer,
    }

    return render(request, 'profile.html', context)
