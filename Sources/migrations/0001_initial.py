# Generated by Django 5.0.3 on 2024-03-23 20:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AnimeTitles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('website', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ExternalReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField()),
                ('author_name', models.CharField(max_length=100)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('anime_title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AnimeTitles.animetitle')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Sources.source')),
            ],
        ),
    ]
