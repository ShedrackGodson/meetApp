# Generated by Django 3.0.3 on 2020-03-08 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('group_location', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Not Interested', 'Not Interested')], max_length=255)),
                ('group_desc', models.TextField(max_length=1000)),
                ('group_topics', models.ManyToManyField(to='group.Topics')),
            ],
        ),
    ]
