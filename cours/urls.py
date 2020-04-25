from django.urls import path
from django.conf.urls import url, include
from . import views

app_name = 'courses'

urlpatterns = [

    path('', views.CoursesListView.as_view(), name='cours'),
    path('<int:pk>/', views.CoursesDetailView.as_view(), name='details'),
    path('tinymce/', include('tinymce.urls')),

]