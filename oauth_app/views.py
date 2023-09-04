from django.shortcuts import redirect,render 
from django.contrib.auth import logout




def twitter_login(request):
    return render(request, 'oauth_app/index.html')

def twitter_logout(request):
    logout(request)
    return redirect('login')

def twitter_auth_complete(request):
    return redirect('login')
