# Generated by Django 2.2.13 on 2020-06-13 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eid', models.IntegerField()),
                ('ename', models.CharField(max_length=20)),
                ('eemail', models.EmailField(max_length=254)),
                ('econtact', models.CharField(max_length=12)),
            ],
            options={
                'db_table': 'emp',
            },
        ),
    ]
