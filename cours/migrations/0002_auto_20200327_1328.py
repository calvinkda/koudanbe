# Generated by Django 3.0.3 on 2020-03-27 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cours', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classes',
            options={'verbose_name': 'Cours', 'verbose_name_plural': 'Cours'},
        ),
        migrations.AlterModelOptions(
            name='courses',
            options={'verbose_name': 'Formation', 'verbose_name_plural': 'Formations'},
        ),
        migrations.AddField(
            model_name='courses',
            name='category',
            field=models.CharField(choices=[('glo', 'Genie Logiciel 2'), ('grh', 'Gestion Des Ressources Humaines 1'), ('math', 'Mathématique 2')], default=1, max_length=8),
            preserve_default=False,
        ),
    ]
