# Generated by Django 3.2 on 2021-04-30 23:29

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sports', models.CharField(max_length=256)),
                ('users', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MentalFitnessAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('o_confidence', models.PositiveSmallIntegerField(default=0, null=True, validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(10)])),
                ('o_concentration', models.PositiveSmallIntegerField(default=0, null=True, validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(10)])),
                ('o_composure', models.PositiveSmallIntegerField(default=0, null=True, validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(10)])),
                ('o_challenge', models.PositiveSmallIntegerField(default=0, null=True, validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(10)])),
                ('o_commitment', models.PositiveSmallIntegerField(default=0, null=True, validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(10)])),
                ('total', models.PositiveSmallIntegerField(default=0, null=True, validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(50)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('text', models.TextField(max_length=2048)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Confidence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('confidence_1', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('confidence_2', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('confidence_3', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('confidence_4', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('confidence_5', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('p_confidence', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(10)])),
                ('mfa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.mentalfitnessassessment')),
            ],
        ),
        migrations.CreateModel(
            name='Concentration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concentration_1', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('concentration_2', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('concentration_3', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('concentration_4', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('concentration_5', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('p_concentration', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(10)])),
                ('mfa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.mentalfitnessassessment')),
            ],
        ),
        migrations.CreateModel(
            name='Composure',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('composure_1', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('composure_2', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('composure_3', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('composure_4', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('composure_5', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('p_composure', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(10)])),
                ('mfa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.mentalfitnessassessment')),
            ],
        ),
        migrations.CreateModel(
            name='Commitment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commitment_1', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('commitment_2', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('commitment_3', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('commitment_4', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('commitment_5', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('p_commitment', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(10)])),
                ('mfa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.mentalfitnessassessment')),
            ],
        ),
        migrations.CreateModel(
            name='Challenge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('challenge_1', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('challenge_2', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('challenge_3', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('challenge_4', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('challenge_5', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(2)])),
                ('p_challenge', models.PositiveSmallIntegerField(validators=[django.core.validators.MinLengthValidator(0), django.core.validators.MaxLengthValidator(10)])),
                ('mfa_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.mentalfitnessassessment')),
            ],
        ),
    ]
