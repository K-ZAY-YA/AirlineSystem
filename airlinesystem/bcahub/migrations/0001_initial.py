# Generated by Django 4.2.5 on 2023-12-03 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operating_date', models.DateTimeField()),
                ('airline', models.CharField(max_length=20)),
                ('airline_name', models.CharField(max_length=20)),
                ('airline_nO', models.IntegerField(verbose_name=10)),
                ('depature_port', models.CharField(max_length=10)),
                ('depature_date_time', models.DateTimeField()),
                ('arrival_date_time', models.DateTimeField()),
                ('flight_status', models.CharField(max_length=10)),
                ('delay_issue', models.CharField(max_length=10)),
                ('remarks', models.CharField(max_length=10)),
                ('action', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Crew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.CharField(max_length=20)),
                ('service_status', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=20)),
                ('depature_port', models.CharField(max_length=10)),
                ('arrival_port', models.CharField(max_length=10)),
                ('depature_date_time', models.DateTimeField()),
                ('arrival_date_time', models.DateTimeField()),
                ('action', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='journeysearch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(verbose_name=5)),
                ('name', models.CharField(max_length=20)),
                ('dob', models.IntegerField(verbose_name=10)),
                ('father', models.CharField(max_length=20)),
                ('passport', models.IntegerField(verbose_name=10)),
                ('gender', models.CharField(max_length=10)),
                ('flightname', models.CharField(max_length=20)),
                ('sector', models.CharField(max_length=10)),
                ('depature_date_time', models.DateTimeField()),
                ('arrival_date_time', models.DateTimeField()),
                ('risk_Satus', models.CharField(max_length=10)),
                ('action', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Riskaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.IntegerField(verbose_name=5)),
                ('name', models.CharField(max_length=20)),
                ('dob', models.IntegerField(verbose_name=10)),
                ('father', models.CharField(max_length=20)),
                ('passport', models.IntegerField(verbose_name=10)),
                ('gender', models.CharField(max_length=10)),
                ('nrc', models.CharField(max_length=50)),
                ('nationality', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
                ('action', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Traveller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.CharField(max_length=20)),
                ('timeframe', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('dob', models.IntegerField(verbose_name=10)),
                ('nrc', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=6)),
                ('depature_port', models.CharField(max_length=10)),
                ('depature_date_time', models.DateTimeField()),
                ('arrival_port', models.CharField(max_length=10)),
                ('arrival_date_time', models.DateTimeField()),
                ('action', models.CharField(blank=True, max_length=10, null=True)),
            ],
        ),
    ]
