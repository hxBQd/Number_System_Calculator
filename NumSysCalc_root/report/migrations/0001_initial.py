# Generated by Django 4.1.1 on 2023-02-05 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="TelegramSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("chat_id", models.CharField(max_length=50, verbose_name="id чата")),
                ("token", models.CharField(max_length=75, verbose_name="token бота")),
                ("mess_temlate", models.TextField(verbose_name="Шаблон сообщения")),
            ],
            options={
                "verbose_name": "Настройка",
                "verbose_name_plural": "Настройки",
            },
        ),
    ]