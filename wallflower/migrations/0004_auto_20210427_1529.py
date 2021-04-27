# Generated by Django 3.1.7 on 2021-04-27 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallflower', '0003_auto_20210426_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='FrontlineUpliftingNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200, verbose_name='Headline')),
                ('description', models.TextField(max_length=400, verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Article Image')),
                ('author', models.CharField(max_length=150, verbose_name='Author')),
                ('source', models.TextField(max_length=200, verbose_name='News Source')),
            ],
            options={
                'verbose_name': "Frontline User's Uplifting News",
                'verbose_name_plural': 'Frontline User Uplifting News',
            },
        ),
        migrations.CreateModel(
            name='IsolatedUpliftingNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200, verbose_name='Headline')),
                ('description', models.TextField(max_length=400, verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Article Image')),
                ('author', models.CharField(max_length=150, verbose_name='Author')),
                ('source', models.TextField(max_length=200, verbose_name='News Source')),
            ],
            options={
                'verbose_name': "Isolated User's Uplifting News",
                'verbose_name_plural': 'Isolated User Uplifting News',
            },
        ),
        migrations.CreateModel(
            name='LossUpliftingNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200, verbose_name='Headline')),
                ('description', models.TextField(max_length=400, verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Article Image')),
                ('author', models.CharField(max_length=150, verbose_name='Author')),
                ('source', models.TextField(max_length=200, verbose_name='News Source')),
            ],
            options={
                'verbose_name': "Loss User's Uplifting News",
                'verbose_name_plural': 'Loss User Uplifting News',
            },
        ),
        migrations.CreateModel(
            name='MentalHealthUpliftingNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200, verbose_name='Headline')),
                ('description', models.TextField(max_length=400, verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Article Image')),
                ('author', models.CharField(max_length=150, verbose_name='Author')),
                ('source', models.TextField(max_length=200, verbose_name='News Source')),
            ],
            options={
                'verbose_name': "Mental Health's Uplifting News",
                'verbose_name_plural': 'Mental Health Uplifting News',
            },
        ),
        migrations.CreateModel(
            name='UnemployedUpliftingNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=200, verbose_name='Headline')),
                ('description', models.TextField(max_length=400, verbose_name='Description')),
                ('image', models.ImageField(upload_to='', verbose_name='Article Image')),
                ('author', models.CharField(max_length=150, verbose_name='Author')),
                ('source', models.TextField(max_length=200, verbose_name='News Source')),
            ],
            options={
                'verbose_name': "Unemployed User's Uplifting News",
                'verbose_name_plural': 'Unemployed User Uplifting News',
            },
        ),
        migrations.DeleteModel(
            name='FrontlineUpliftingContent',
        ),
        migrations.DeleteModel(
            name='IsolatedUpliftingContent',
        ),
        migrations.DeleteModel(
            name='LossUpliftingContent',
        ),
        migrations.DeleteModel(
            name='MentalHealthUpliftingContent',
        ),
        migrations.DeleteModel(
            name='UnemployedUpliftingContent',
        ),
    ]