from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import SignUpForm, User
from .models import *
from . import forms
from . import scrape_BUYMA

from django.shortcuts import get_object_or_404, render, redirect

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

            # Usage = get_object_or_404(UserUsageSituation, )
            last_usage = UserUsageSituation.objects.last()
            
            new_usage= UserUsageSituation.objects.create(user_id = request.user)
            new_usage.display_count = last_usage.display_count + 1
            new_usage.research_count = last_usage.research_count + 1
            new_usage.save()

        # research_count=new_usage.research_count
        # ctxt = self.get_context_data(research_count = research_count)
        # return render(                                                                 
        #     request,                                                                     
        #     'registration/index.html',                                               
        #     ctxt,
        #     response                                                                      
        # ) 
        return response


def csvexport(data_buyma):
    # csvファイルを作るコード
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;  filename="filename.csv"'


# ここからcsvの内容を編集コード
    data_buyma.to_csv(path_or_buf=response, encoding='utf_8_sig', index=None)

    return response

