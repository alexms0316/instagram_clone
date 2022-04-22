# Generated by Django 4.0.4 on 2022-04-22 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_remove_user_name_remove_user_phone_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=10000, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postings', to='users.user')),
            ],
            options={
                'db_table': 'postings',
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_url', models.URLField(max_length=2000)),
                ('image_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='postings.posting')),
            ],
            options={
                'db_table': 'images',
            },
        ),
    ]