from django.shortcuts import render
from cours.models import Courses, Classes
from django.views.generic import ListView, DetailView


class CoursesListView(ListView):
    template_name = 'cours/index.html'
    model = Courses
    context_object_name = 'courses'


class CoursesDetailView(DetailView):
    template_name = 'cours/single.html'
    model = Courses
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context