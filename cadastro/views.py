from django.http import HttpResponse


def index(request):
    return HttpResponse("COMEÇANDO O TRABALHO")


