# Generated by Django 2.0.5 on 2018-06-17 08:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_zh', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Commodity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_zh', models.CharField(max_length=50)),
                ('describe', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_zh', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('city', models.CharField(max_length=50)),
                ('town', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_zh', models.CharField(max_length=50)),
                ('date', models.CharField(max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_search.Company')),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_zh', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_zh', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('token', models.AutoField(primary_key=True, serialize=False)),
                ('name_zh', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_search.Bank')),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='own_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='own_person', to='main_search.User'),
        ),
        migrations.AddField(
            model_name='record',
            name='quest_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quest_person', to='main_search.User'),
        ),
        migrations.AddField(
            model_name='record',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_search.Type'),
        ),
        migrations.AddField(
            model_name='commodity',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_search.Location'),
        ),
        migrations.AddField(
            model_name='commodity',
            name='own_person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_search.User'),
        ),
        migrations.AddField(
            model_name='commodity',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_search.State'),
        ),
        migrations.AddField(
            model_name='commodity',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_search.Type'),
        ),
    ]
