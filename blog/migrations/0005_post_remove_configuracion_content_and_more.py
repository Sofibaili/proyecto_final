# Generated by Django 4.1.2 on 2022-10-31 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_configuracion_subtitulo_principal_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_content', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=3000)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='configuracion',
            name='content',
        ),
        migrations.RemoveField(
            model_name='configuracion',
            name='date_published',
        ),
        migrations.RemoveField(
            model_name='configuracion',
            name='short_content',
        ),
        migrations.RemoveField(
            model_name='configuracion',
            name='title',
        ),
        migrations.AddField(
            model_name='configuracion',
            name='nombre_blog',
            field=models.CharField(default=0, max_length=14),
            preserve_default=False,
        ),
    ]
