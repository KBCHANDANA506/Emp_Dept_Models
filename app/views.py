from django.shortcuts import render
from app.models import *
from django.db.models import Q
# Create your views here.
def Display_Dept(request):
    TOD=Department.objects.all()
    
    #like operations startswith,endswith
    TOD=Department.objects.filter(DNAME__startswith='s')
    TOD=Department.objects.filter(DNAME__endswith='s')
    #TOD=Department.objects.filter(Q(DNAME__startsswith='s')&Q(DNAME__endswith='s'))
    TOD=Department.objects.all()


    d={'dept':TOD}
    return render(request,'Display_Dept.html',d)

def Display_emp(request):
    TOE=EMPLOYEE.objects.all()
    #date lookups
    TOE=EMPLOYEE.objects.filter(HIREDATE__year__gt='1981')
    TOE=EMPLOYEE.objects.filter(HIREDATE__year='1981')
    TOE=EMPLOYEE.objects.filter(HIREDATE__month='09')
    TOE=EMPLOYEE.objects.filter(HIREDATE__year='1981')
    TOE=EMPLOYEE.objects.filter(HIREDATE__day='23')
    #like operations startswith,endswith
    TOE=EMPLOYEE.objects.filter(ENAME__startswith='A')
    TOE=EMPLOYEE.objects.filter(ENAME__endswith='N')
    #contains
    TOE=EMPLOYEE.objects.filter(ENAME__contains='ALLEN')
    TOE=EMPLOYEE.objects.filter(ENAME__contains=('KING'))
    #IN
    TOE=EMPLOYEE.objects.filter(ENAME__in=('KING','PRESIDENT','7839'))
    #regex
    TOE=EMPLOYEE.objects.filter(ENAME__regex='[a-ZA-Z](4)')
    #Queryset
    TOE=EMPLOYEE.objects.filter(ENAME__endswith='N')
    TOE=EMPLOYEE.objects.all()



    d={'emp':TOE}
    return render(request,'Display_emp.html',d)