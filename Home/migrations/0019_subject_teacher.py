# Generated by Django 3.1 on 2020-08-27 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0018_auto_20200827_1330'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('experience', models.DecimalField(decimal_places=2, max_digits=4)),
                ('classes', models.CharField(choices=[('1-5', 'First to Fifth'), ('6-8', 'Sixth to Eighth'), ('9-10', 'Ninth to Tenth'), ('11-12', 'Eleventh to Twelfth'), ('9-12', 'Ninth to Twelfth')], max_length=6)),
                ('phone', models.CharField(max_length=10)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='teachers/%Y/%m/%D/')),
                ('teacher_type', models.CharField(blank=True, choices=[('Home Tutor', 'HT'), ('Tution Center Teacher', 'TT')], max_length=30)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Home.location')),
                ('subject1', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject1', to='Home.subject')),
                ('subject2', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject2', to='Home.subject')),
                ('subject3', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='subject3', to='Home.subject')),
            ],
        ),
    ]