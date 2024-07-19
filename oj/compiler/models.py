from django.db import models
from django.contrib.auth.models import User

# Create your models here.

from home.models import Problems
from django.db import models

class CodeSubmission(models.Model):
    LANGUAGE_CHOICES = [
        ("py", "Python"),
        ("c", "C"),
        ("cpp", "C++"),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problems, on_delete=models.CASCADE) 
    language = models.CharField(max_length=3, choices=LANGUAGE_CHOICES)
    code = models.TextField()
    input_data = models.TextField(blank=True, null=True)
    output_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    verdict = models.CharField(max_length = 10)

    def __str__(self):
        return f"{self.problem.p_name} - {self.user.username} - {self.language}"
