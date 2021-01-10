# Generated by Django 3.0.6 on 2021-01-08 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku_id', models.CharField(blank=True, max_length=10, null=True)),
                ('product_id', models.CharField(blank=True, max_length=10, null=True)),
                ('sku_name', models.CharField(blank=True, max_length=30, null=True)),
                ('price', models.IntegerField(blank=True, max_length=30, null=True)),
                ('manufacturer_name', models.CharField(blank=True, max_length=30, null=True)),
                ('salt_name', models.CharField(blank=True, max_length=30, null=True)),
                ('drug_form', models.CharField(blank=True, max_length=30, null=True)),
                ('pack_size', models.CharField(blank=True, max_length=30, null=True)),
                ('strength', models.CharField(blank=True, max_length=30, null=True)),
                ('product_banned', models.CharField(blank=True, max_length=30, null=True)),
                ('unit', models.CharField(blank=True, max_length=30, null=True)),
                ('price_per_unit', models.IntegerField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]