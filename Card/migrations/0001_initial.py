# Generated by Django 3.1.6 on 2021-02-23 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('card_id', models.IntegerField(primary_key=True, serialize=False)),
                ('card_in_deck', models.BooleanField(default=True)),
                ('card_in_discard', models.BooleanField(default=False)),
                ('card_on_top', models.BooleanField(default=False)),
                ('card_in_hand', models.IntegerField(default=0)),
                ('card_is_playable', models.BooleanField(default=False)),
                ('card_color', models.CharField(choices=[('BLACK', 'BLACK'), ('RED', 'RED'), ('YELLOW', 'YELLOW'), ('GREEN', 'GREEN'), ('BLUE', 'BLUE')], default='BLACK', max_length=10)),
                ('card_value', models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('SKIP', 'SKIP'), ('REVERSE', 'REVERSE'), ('PLUS TWO', 'PLUS TWO'), ('CHANGE COLOR', 'CHANGE COLOR'), ('PLUS FOUR AND CHANGE COLOR', 'PLUS FOUR AND CHANGE COLOR')], default=0, max_length=30)),
            ],
        ),
    ]
