from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
#from tinymce import models as tinymce_models
from ckeditor.fields import RichTextField

User = get_user_model()


class TimeStampModel(models.Model):
    created_at = models.DateField(auto_now=False, auto_now_add=True)
    updated_at = models.DateField(auto_now=True, auto_now_add=False)

    class Meta:
        abstract = True

# Create your models here.


class Courses(TimeStampModel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    slug = models.SlugField()
    category = models.CharField(max_length=8, choices=(('glo', 'Genie Logiciel 2'), (
        'grh', 'Gestion Des Ressources Humaines 1'), ('math', 'Mathématique 2')))
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Formation'
        verbose_name_plural = 'Formations'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('courses:details', kwargs={'pk': self.pk})


class Classes(TimeStampModel):
    content = RichTextField()
    course = models.ForeignKey(
        Courses, on_delete=models.CASCADE, related_name='classes')

    class Meta:
        verbose_name = 'Cours'
        verbose_name_plural = 'Cours'
