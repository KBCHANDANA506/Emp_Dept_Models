from django.db import models

# Create your models here.
class Department(models.Model):
    DEPTNO=models.IntegerField(max_length=100,primary_key=True)
    DNAME=models.CharField(max_length=100)
    LOC=models.CharField(max_length=100)

    def __str__(self):
        return self.DNAME


class EMPLOYEE(models.Model):
    EMPNO=models.IntegerField(max_length=100,primary_key=True)
    ENAME=models.CharField(max_length=100)
    JOB=models.CharField(max_length=100)
    MGR=models.IntegerField()
    HIREDATE=models.DateField()
    SAL=models.IntegerField()
    COMM=models.IntegerField()
    DEPTNO=models.ForeignKey(Department,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.ENAME
