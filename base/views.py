from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

import stripe


#secret

stripe.api_key = "sk_test_51ID2ptJwaTxNfjS7t04ElE3rlY3744PmH8jXevFvOknCuIyFaJ1BWo116MWS8R8QwWfXF4r3K4ZPOhyEYZpNXTmv003oezekBJ"


# Create your views here.

def index(request):
	return render(request, 'base/index.html')


def charge(request):


	if request.method == 'POST':
		print('Data:', request.POST)
		

		amount = int(request.POST['amount'])
		print("@@@@@@@@@@@@@")
		print(amount)

	return redirect(reverse('success', args=[amount]))



def successMsg(request, args):
	amount = args
	return render(request, 'base/success.html', {'amount':amount})