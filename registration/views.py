from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import SignUpForm

from . import forms
from . import scrape_BUYMA

from django.shortcuts import render, redirect

from django.http import HttpResponse


class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class Index_view(FormView):
    form_class = forms.TextForm
    template_name = 'registration/index.html'

    def form_valid(self, form):
        data = form.cleaned_data
        search = data["search"]
        limit = data["limit"]
        request = self.request

        if request.method == 'POST':
            data_buyma = scrape_BUYMA.sea(search, limit)
            response = csvexport(data_buyma)


        return response


def csvexport(data_buyma):
    # csvファイルを作るコード
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;  filename="filename.csv"'


# ここからcsvの内容を編集コード
    # writer.writerow(data_buyma)
    data_buyma.to_csv(path_or_buf=response, encoding='utf_8_sig', index=None)

    return response

