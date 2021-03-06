from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import UserProfile
from donation.models import Donation
from donation.forms import Amount


@login_required
def profile(request):
    """ Return profile page """
    profile = get_object_or_404(UserProfile, user=request.user)
    donations = Donation.objects.filter(email=request.user.email)
    amounts = Amount()
    context = {
        'profile': profile,
        'donations': donations,
        'amounts': amounts
    }
    return render(request, 'profiles/profiles.html', context)

