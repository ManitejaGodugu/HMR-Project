from django.db import models

# Create your models here.
class Department(models.Model):
    DEPT_STATUS_CHOICES = (
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    )

    dept_id = models.AutoField(primary_key=True)
    dept_name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=50, choices=DEPT_STATUS_CHOICES, default='active')

    def __str__(self):
        return self.dept_name