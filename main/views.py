from django.views import View
from django.shortcuts import render, redirect


class MainView(View):
    def get(self, request):
        try:
            member = request.session['member']
        except KeyError:
            member = None

        return render(request, 'main.html', {'member': member})
