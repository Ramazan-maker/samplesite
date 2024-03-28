# Generated by Django 4.2.7 on 2024-03-28 14:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('testapp', '0007_alter_img_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='PGSProject',
        ),
        migrations.DeleteModel(
            name='PGSProject2',
        ),
        migrations.DeleteModel(
            name='PGSProject3',
        ),
        migrations.DeleteModel(
            name='PGSRoomReserving',
        ),
        migrations.DeleteModel(
            name='PGSRubric',
        ),
        migrations.DeleteModel(
            name='PrivateMessage',
        ),
    ]
