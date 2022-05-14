# Generated by Django 4.0.4 on 2022-05-14 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accounts',
            fields=[
                ('AccountID', models.AutoField(primary_key=True, serialize=False)),
                ('Username', models.CharField(max_length=300)),
                ('Password', models.CharField(max_length=200)),
                ('Type', models.CharField(max_length=1)),
                ('DateCreate', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('AttendanceID', models.AutoField(primary_key=True, serialize=False)),
                ('Status', models.BooleanField(default=False)),
                ('Note', models.CharField(max_length=300, null=True)),
                ('Username', models.CharField(max_length=300)),
                ('ListAttendanceID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('ClassID', models.AutoField(primary_key=True, serialize=False)),
                ('ClassCode', models.CharField(max_length=300, null=True)),
                ('ClassName', models.CharField(max_length=500, null=True)),
                ('Schedule', models.CharField(max_length=300, null=True)),
                ('TotalStu', models.CharField(max_length=300, null=True)),
                ('DateCreate', models.DateField(auto_now=True)),
                ('TeacherID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ListAttendance',
            fields=[
                ('ListAttendanceID', models.AutoField(primary_key=True, serialize=False)),
                ('Date', models.DateField(auto_now=True)),
                ('Time', models.TimeField(auto_now=True)),
                ('Total', models.IntegerField(null=True)),
                ('ClassID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('StudentID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=500, null=True)),
                ('Gentle', models.CharField(max_length=1)),
                ('StudentCode', models.CharField(max_length=300, null=True)),
                ('DateOfBirth', models.DateField(null=True)),
                ('Email', models.CharField(max_length=300, null=True)),
                ('Avatar', models.CharField(max_length=300, null=True)),
                ('Username', models.CharField(max_length=300)),
                ('ClassID', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teachers',
            fields=[
                ('TeacherID', models.AutoField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=500, null=True)),
                ('Email', models.CharField(max_length=300, null=True)),
                ('Phone', models.CharField(max_length=300, null=True)),
                ('Avatar', models.ImageField(null=True, upload_to='')),
                ('Username', models.CharField(max_length=300)),
            ],
        ),
    ]
