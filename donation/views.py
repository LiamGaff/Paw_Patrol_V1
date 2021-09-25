from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

import stripe


def donate(request):
    """ return doante page """

    return render(request, "donation/donate.html")


def charge(request):
    amount = 5
    if request.method == 'POST':
        print('Data:', request.POST )
    return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
        
        amount = args
        return render(request, "donation/success.html", {'amount':amount})