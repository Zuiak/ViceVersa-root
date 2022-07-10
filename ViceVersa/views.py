from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    usertext = request.GET['usertext']
    reversed_usertext = usertext[::-1]
    return render(request, 'reverse.html', {'usertext': usertext, 'reversed_usertext': reversed_usertext})
