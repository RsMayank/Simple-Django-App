from django.urls import path
from . import views

# 
# app_name = 'myApp'
# urlpatterns =[
#     #ie myApp/5/
#     path('<int:question_id>/',views.detail,name='detail'),
#     #ie myApp/5/result
#     path('<int:question_id>/results/',views.results,name = 'results'),

#     #ie myApp/5/vote
#     path('<int:question_id>/vote/',views.vote,name = 'vote'),
#     path('',views.index,name ='index')
# ]

# we can use generic view to avoid rewriting the redundent code.

app_name = 'myApp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]