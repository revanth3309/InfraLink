# Generated by Django 5.1.1 on 2024-09-14 10:37

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infra', '0005_post_replie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=255)),
                ('priority', models.IntegerField(choices=[(1, 'High'), (2, 'Medium'), (3, 'Low')], default=2)),
                ('due_date', models.DateField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='infra.project')),
            ],
        ),
    ]
