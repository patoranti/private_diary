import logging

from django.urls import  reverse_lazy
from django.views import  generic
from.forms import InquiryForm
from django.contrib import  messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Diary


logger = logging.getLogger(__name__)

class IndexView(generic.TemplateView):
    template_name = "index.html" #画面表示

class GoodView(generic.TemplateView):
    template_name = "good.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm #forms.py
    success_url = reverse_lazy('diary:inquiry') #リダイレクト、画面遷移

    def form_valid(self, form): #親クラスで定義されているメソッド、オーバーライド
        form.send_email() #forms.pyのsend_email
        messages.success(self.request,'メッセージを送信しました')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)

class DiaryListView(LoginRequiredMixin,generic.ListView): #ログインしているユーザしか一覧を見れない設定
    model = Diary #modelを使って表示
    template_name = 'diary_list.html'

    def get_queryset(self):
        diaries = Diary.objects.filter(user=self.request.user).order_by('-created_at') #公開、非公開設定
        return diaries
