# Generated by Django 2.0.7 on 2018-07-16 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GPIO_pins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin', models.PositiveIntegerField(choices=[('5', '5'), ('6', '6'), ('13', '13'), ('19', '19'), ('26', '26'), ('21', '21'), ('20', '20'), ('16', '16')])),
                ('gpio_state', models.CharField(blank=True, choices=[('OUT', 'OUT'), ('IN', 'IN')], max_length=200)),
                ('default_state', models.BooleanField(default=False)),
            ],
        ),
    ]