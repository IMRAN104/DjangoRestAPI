# Generated by Django 2.2.6 on 2020-08-14 07:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(
                    blank=True, max_length=100, null=True)),
                ('psot_desscription', models.TextField(
                    blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
