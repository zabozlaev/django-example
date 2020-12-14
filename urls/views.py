from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseNotFound
from django.shortcuts import redirect
from .forms import CreateUrlForm
from .models import Url
from hashlib import md5

# Create your views here.


class CreateUrlView(generic.CreateView):
    form = CreateUrlForm()

    def get(self, request, *args, **kwargs):
        return render(request, 'urls/create.html', {'form': CreateUrlForm})

    def post(self, request, *args, **kwargs):
        form = CreateUrlForm(request.POST)
        if form.is_valid():
            new_url = Url()
            new_url.source_url = form.cleaned_data['url']
            new_url.short_url = md5(new_url.source_url.encode('utf-8')).hexdigest()[:10]
            new_url.save()
        # отобразить страницу и передать новый урл
        return render(request, 'urls/create.html', {
            'created_url': new_url
        })


def index_url_view(req, short):
    if req.method == 'GET':
        found_url = Url.objects.get(short_url=short)
        return redirect(found_url.source_url) if found_url else HttpResponseNotFound('Url not found')
