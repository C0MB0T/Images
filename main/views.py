from django.shortcuts import render
from . import models


def index(request):
    context = {
        'm': models.SetImage.objects.all(),
    }
    return render(request, 'main/index.html', context)