# Generated by Django 4.2.4 on 2023-08-14 00:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('community', '0008_compost_comcomments_cnt'),
        ('main', '0013_mainpost_jebo_bool'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MyRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainposts', models.ManyToManyField(blank=True, related_name='myrequests', to='main.mainpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myrequests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainposts', models.ManyToManyField(blank=True, related_name='myreports', to='main.mainpost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myreports', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyComPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('composts', models.ManyToManyField(related_name='mycomposts', to='community.compost')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mycomposts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MyCom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comcomments', models.ManyToManyField(blank=True, related_name='mycoms', to='community.comcomment')),
                ('comreplies', models.ManyToManyField(blank=True, related_name='mycoms', to='community.comreply')),
                ('maincomments', models.ManyToManyField(blank=True, related_name='mycoms', to='main.maincomment')),
                ('mainreplies', models.ManyToManyField(blank=True, related_name='mycoms', to='main.mainreply')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mycommentsreplies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
