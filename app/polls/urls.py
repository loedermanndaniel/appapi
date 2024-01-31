from django.urls import path, include
from .views import index, PollDetailView, vote, ResultsDetailView
from django.views.generic.base import TemplateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from django.contrib import admin

app_name = 'polls'

urlpatterns = [
    path('', index, name="index"),
    path("admin/", admin.site.urls),
    #path('', TemplateView.as_view(template_name="polls/index.html"), name="index"),
    path('poll/<str:slug>', PollDetailView.as_view(), name="umfrage-detail"),
    path('poll/<str:slug>/vote/', vote, name='vote'),
    path('poll/<str:slug>/results/', ResultsDetailView.as_view(), name='results'),
    path('account/', include("django.contrib.auth.urls")),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

]