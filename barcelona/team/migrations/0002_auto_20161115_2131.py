# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 20:06
from __future__ import unicode_literals
import csv
from django.db import migrations


def add_player(apps, schema_editor):
    Player = apps.get_model("team", "Player")
    with open('squad.csv') as f:
        reader = csv.reader(f, delimiter=',')
        print(reader)
        for i in reader:
            print(i)
            pl = Player(pos=i[0], no=i[1], player=i[2], age=i[3], gs=i[4],
             sb=i[5], g=i[6],sh=i[7], sg=i[8], a=i[9], fc=i[10], fs=i[11], yc=i[12], rc=i[13])
            pl.save()


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_player)
    ]
