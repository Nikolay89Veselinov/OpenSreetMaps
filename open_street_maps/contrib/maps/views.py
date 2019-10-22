from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponse

from .forms import OpenStreetMapsForm
from .models import OpenStreetMaps


class MyCreateView(CreateView):
    form_class = OpenStreetMapsForm
    model = OpenStreetMaps


def map(request):

    if request.method == 'POST':
        form = OpenStreetMapsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('success')
    else:
        form = OpenStreetMapsForm(request.POST)
    context = {
        'form': form,
    }

    return render(request, 'forms.html', context)

