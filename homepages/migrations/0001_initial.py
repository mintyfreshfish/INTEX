# Generated by Django 3.1.2 on 2020-12-07 21:41

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplicant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant_email', models.CharField(max_length=25)),
                ('applicant_phone', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=25)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='JobListing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=50)),
                ('contracts', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=3000)),
            ],
        ),
        migrations.CreateModel(
            name='JobOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50)),
                ('company_email', models.CharField(max_length=25)),
                ('company_phone', models.CharField(max_length=10)),
                ('street_address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('zip', models.CharField(max_length=25)),
                ('size', models.CharField(max_length=2)),
                ('sector', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='JobOffersMade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepages.jobapplicant')),
                ('job_listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepages.joblisting')),
            ],
        ),
        migrations.CreateModel(
            name='JobListingSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_level', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)])),
                ('job_listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepages.joblisting')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepages.skill')),
            ],
        ),
        migrations.AddField(
            model_name='joblisting',
            name='organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepages.joborganization'),
        ),
        migrations.CreateModel(
            name='JobApplicantSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_level', models.PositiveIntegerField(default=1, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(4)])),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepages.jobapplicant')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepages.skill')),
            ],
        ),
    ]
