from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('/', views.index, name = "index"),
    path('/create/', views.create, name = "create"),
    path('/<slug:slug>/', views.show, name = "show"),
    # path('writer/', views.writer),
]