from django.shortcuts import render

def text(request):
    return render(request, 'ViceVersa.html')

def reverse(request):
    user_text = request.GET['usertext']
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html', {'usertext': reversed_text})
