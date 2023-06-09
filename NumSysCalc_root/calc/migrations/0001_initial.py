# Generated by Django 4.1.5 on 2023-03-03 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MathExpression',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isRight', models.BooleanField(default=True)),
                ('initial_num', models.CharField(default='0', max_length=50)),
                ('initial_sys', models.IntegerField(choices=[('2', None), ('3', None), ('4', None), ('5', None), ('6', None), ('7', None), ('8', None), ('9', None), ('10', None), ('11', None), ('12', None), ('13', None), ('14', None), ('15', None), ('16', None), ('17', None), ('18', None), ('19', None), ('20', None), ('21', None), ('22', None), ('23', None), ('24', None), ('25', None), ('26', None), ('27', None), ('28', None), ('29', None), ('30', None), ('31', None), ('32', None), ('33', None), ('34', None), ('35', None), ('36', None)], default=(10, None))),
                ('next_sys', models.IntegerField(choices=[('2', None), ('3', None), ('4', None), ('5', None), ('6', None), ('7', None), ('8', None), ('9', None), ('10', None), ('11', None), ('12', None), ('13', None), ('14', None), ('15', None), ('16', None), ('17', None), ('18', None), ('19', None), ('20', None), ('21', None), ('22', None), ('23', None), ('24', None), ('25', None), ('26', None), ('27', None), ('28', None), ('29', None), ('30', None), ('31', None), ('32', None), ('33', None), ('34', None), ('35', None), ('36', None)], default=(10, None))),
                ('next_num', models.CharField(default='0', max_length=50)),
            ],
        ),
    ]
