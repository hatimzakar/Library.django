# Generated by Django 3.0.6 on 2020-06-11 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20200610_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField(max_length=100)),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('numeroProduit', models.IntegerField(max_length=100)),
                ('quantite', models.IntegerField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='produit',
            name='numero',
            field=models.IntegerField(max_length=100),
        ),
    ]
