from django.db import models

# Create your models here.
class Problems(models.Model):
    statement = models.CharField(max_length=5000)
    p_name = models.CharField(max_length=100)

    def __str__(self):
        return self.p_name




class test_cases(models.Model):
    input = models.CharField(max_length=100)
    output = models.CharField(max_length=100)
    problem = models.ForeignKey(Problems, on_delete= models.CASCADE)
    
    def __str__(self):
        return f"TestCase for {self.problem.p_name}"