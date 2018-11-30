# Generated by Django 2.0.2 on 2018-06-20 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='eleccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eleccion_texto', models.CharField(max_length=100)),
                ('votos', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='pregunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregunta_texto', models.CharField(max_length=100)),
                ('pub_calendario', models.DateTimeField(verbose_name='Fecha de publicacion')),
            ],
        ),
        migrations.AddField(
            model_name='eleccion',
            name='preguntas',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.pregunta'),
        ),
    ]