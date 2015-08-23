# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('doc', models.DateField(auto_now_add=True, verbose_name='Date Of Creation')),
                ('dom', models.DateField(auto_now=True, verbose_name='Last modified')),
                ('summary', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=1200)),
                ('source', models.URLField()),
                ('images', models.ImageField(upload_to='images/%D')),
                ('positive_votes', models.IntegerField(default=0)),
                ('negative_votes', models.IntegerField(default=0)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='HealthCentre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('telephone', models.CharField(max_length=120, null='TRUE')),
                ('fax', models.CharField(max_length=120, null='TRUE')),
                ('email', models.EmailField(max_length=254, null='TRUE')),
                ('website', models.URLField(null='TRUE')),
                ('postal_address', models.CharField(max_length=300, null='TRUE')),
                ('physical_address', models.CharField(max_length=300, null='TRUE')),
                ('geo_data', models.CharField(max_length=1200, null='TRUE')),
                ('district', models.CharField(max_length=60)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(verbose_name='Date Of Birth')),
                ('age', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Contraceptive',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, parent_link=True, primary_key=True, serialize=False, to='igirl.Article')),
                ('advantages', models.CharField(max_length=1200)),
                ('disadvantages', models.CharField(max_length=1200)),
            ],
            bases=('igirl.article',),
        ),
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, parent_link=True, primary_key=True, serialize=False, to='igirl.Article')),
                ('treatment', models.CharField(max_length=1200)),
                ('considerations', models.CharField(max_length=1200, null='TRUE')),
                ('protection', models.CharField(max_length=1200)),
            ],
            bases=('igirl.article',),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('article_ptr', models.OneToOneField(auto_created=True, parent_link=True, primary_key=True, serialize=False, to='igirl.Article')),
                ('type', models.ForeignKey(to='igirl.Contraceptive')),
            ],
            bases=('igirl.article',),
        ),
    ]
