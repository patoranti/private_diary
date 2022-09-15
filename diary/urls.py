from django.urls import  path
from . import views #.は同じフォルダにある場合

app_name = 'diary'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('good',views.GoodView.as_view(),name="good"),
    path('inquiry/',views.InquiryView.as_view(),name="inquiry"),
    path('diary-list/',views.DiaryListView.as_view(),name="diary_list"),
]