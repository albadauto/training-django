# Generated by Django 5.1.3 on 2024-11-07 17:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_pessoa_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('Id', models.AutoField(primary_key=True, serialize=False)),
                ('NomeVeiculo', models.TextField(max_length=255)),
                ('pessoa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pessoas', to='home.pessoa')),
            ],
        ),
    ]
