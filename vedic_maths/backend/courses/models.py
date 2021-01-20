from django.db import models

# Create your models here.

class CourseCategories(models.Model):
    category = models.CharField(max_length=150)
    category_description = models.TextField()
    image = models.ImageField(upload_to='categories/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)



class CourseInstructors(models.Model):
    name = models.CharField(max_length=50)
    qualification = models.CharField(max_length=120)
    about = models.TextField()
    Facebook = models.CharField(max_length=150, blank=True, null=True)
    twitter = models.CharField(max_length=150, blank=True, null=True)
    instagram = models.CharField(max_length=150, blank=True, null=True)
    experience = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    photo = models.ImageField(upload_to = 'instractor/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class Courses(models.Model):
    COURSE_CHOUCE = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advance', 'Advance')
    )
    course_name = models.CharField(max_length=150)
    course_category = models.ForeignKey(CourseCategories, on_delete=models.CASCADE)
    course_description = models.TextField()
    instructor = models.ForeignKey(CourseInstructors, on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    course_level = models.CharField(
        max_length=50,
        choices=COURSE_CHOUCE,
        default='Beginner'
    ) 
    thumbnail = models.ImageField(upload_to='thumbnail')
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    price=models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

















