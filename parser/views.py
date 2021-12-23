from django.http.response import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, FormView
import requests
from . import models, forms, parser
# Create your views here.


class GameView(ListView):
    template_name = 'game_index.html'

    def get_queryset(self):
        return models.Game.objects.all()

class ParserGameView(FormView):
    template_name = 'parser.html'
    form_class =  forms.ParserForm
    success_url = '/game/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(requests.POST)
        if form.is_valid():
            form.parse_data()
            return HttpResponse(self.success_url)
        else:
            return super(ParserGameView, self).post(requests, *args, **kwargs)