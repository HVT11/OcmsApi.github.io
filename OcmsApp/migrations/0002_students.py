# Generated by Django 4.0.4 on 2022-05-02 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('OcmsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('StudentID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=500, null=True)),
                ('Gentle', models.CharField(default=1, max_length=1)),
                ('StudentCode', models.CharField(max_length=300, null=True)),
                ('DateOfBirth', models.DateField(null=True)),
                ('Email', models.CharField(max_length=300, null=True)),
                ('Avatar', models.CharField(max_length=300, null=True)),
                ('Username', models.CharField(max_length=300)),
                ('ClassID', models.IntegerField()),
            ],
        ),
    ]