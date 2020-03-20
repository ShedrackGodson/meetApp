# Generated by Django 3.0.3 on 2020-03-11 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0006_delete_organizer'),
        ('users', '0014_profile_is_organizer'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='group_organizing',
            field=models.ManyToManyField(related_name='profile_groups', to='group.MeetAppGroup'),
        ),
    ]
