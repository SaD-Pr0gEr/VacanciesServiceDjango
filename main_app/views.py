from django.shortcuts import render


def hello(request):
    return render(
        request,
        'main_app/index.html'
    )
