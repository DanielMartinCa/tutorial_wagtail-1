# Generated by Django 3.2.11 on 2022-02-24 11:55

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.contrib.taggit
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('wagtailcore', '0066_collection_management_permissions'),
        ('blog', '0007_blogpage_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViajesPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('date', models.DateField(verbose_name='Fecha Post')),
                ('intro', models.CharField(max_length=250, verbose_name='Introducción')),
                ('body', wagtail.core.fields.RichTextField(blank=True)),
                ('categories', modelcluster.fields.ParentalManyToManyField(blank=True, to='blog.BlogCategory')),
                ('tags', modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='blog.BlogPageTag', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
