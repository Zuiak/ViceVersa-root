from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def reverse(request):
    usertext = request.GET['usertext']
    usertext_length = len(usertext.split())
    reversed_usertext = usertext[::-1]
    return render(request, 'reverse.html', {'usertext': usertext, 'usertext_length': usertext_length, 'reversed_usertext': reversed_usertext})
