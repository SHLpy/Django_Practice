import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','module_project3.settings')

import django

django.setup()

from faker import Faker
from testapp.models import Student
from random import *

fake = Faker()#Object creation for Faker class
def phonenumbergen():
	d1 = randint(6,9)
	num = ''+str(d1)
	for i in range(9):
		num += str(randint(0,9))
	return int(num)
def populate(n):
    for i in range(n):
        frollno = fake.random_int(min=1,max=999)
        fname = fake.name()
        fdob = fake.date()
        fmarks = fake.random_int(min=1,max=100)
        femail = fake.email()
        fphonenumber = phonenumbergen()
        faddress = fake.address()
        Student.objects.get_or_create(rollno=frollno,name=fname,dob=fdob, marks=fmarks,email=femail,phonenumber=fphonenumber,address=faddress)
n = int(input('Enter number of students:'))
populate(n)
print(f'{n} Records inserted successfully....')
