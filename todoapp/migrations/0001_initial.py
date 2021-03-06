# Generated by Django 3.1.6 on 2021-02-16 13:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(help_text='Post ID', primary_key=True, serialize=False)),
                ('contents', models.TextField(help_text='post contents')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='post created date')),
                ('updated_at', models.DateTimeField(auto_now_add=True, help_text='post updated date')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(help_text='Comment ID', primary_key=True, serialize=False)),
                ('contents', models.TextField(help_text='Comment contents')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='post created date')),
                ('updated_at', models.DateTimeField(auto_now_add=True, help_text='post updated date')),
                ('post_id', models.ForeignKey(db_column='post_id', on_delete=django.db.models.deletion.CASCADE, related_name='post', to='todoapp.post')),
            ],
        ),
    ]
