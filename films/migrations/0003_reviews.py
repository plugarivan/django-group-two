# Generated by Django 4.1.3 on 2022-12-03 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_direction_genre_alter_film_options_film_url_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=50, verbose_name='Имя')),
                ('text_reviews', models.TextField(max_length=3000, verbose_name='Текст отзыва')),
                ('film', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='films.film', verbose_name='Фильм')),
            ],
            options={
                'verbose_name': 'Отзыв',
                'verbose_name_plural': 'Отзывы',
            },
        ),
    ]
