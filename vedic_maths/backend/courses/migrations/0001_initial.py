# Generated by Django 3.1.5 on 2021-01-19 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=150)),
                ('category_description', models.TextField()),
                ('image', models.ImageField(upload_to='categories/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CourseInstructors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('qualification', models.CharField(max_length=120)),
                ('about', models.TextField()),
                ('Facebook', models.CharField(max_length=150)),
                ('twitter', models.CharField(max_length=150)),
                ('instagram', models.CharField(max_length=150)),
                ('experience', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('photo', models.ImageField(upload_to='instractor/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=150)),
                ('course_description', models.TextField()),
                ('rating', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('course_level', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advance', 'Advance')], default='Beginner', max_length=50)),
                ('thumbnail', models.ImageField(upload_to='thumbnail')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('course_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.coursecategories')),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.courseinstructors')),
            ],
        ),
    ]
