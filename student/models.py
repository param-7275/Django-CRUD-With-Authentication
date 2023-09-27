from django.db import models
class StudentData(models.Model):
    student_name = models.CharField(max_length=50)
    student_address = models.CharField(max_length=50)
    student_contact = models.CharField(max_length=10)
    class Meta:
        verbose_name_plural = "StudentData"
    def __str__(self):
        return self.student_name

    
    



    


    




 