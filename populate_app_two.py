import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N = 5):
    for entry in range(N):
        fakename = fakegen.name().split()
        fakefirstname = fakename[0]
        fakelastname  = fakename[1]
        fakeemail = fakegen.email()

        nextuser = User.objects.get_or_create(first_name=fakefirstname,last_name=fakelastname,email=fakeemail)

if __name__ == "__main__":
    print("Population Script Launched!")
    populate(20)
    print("Population Script Ended!")
