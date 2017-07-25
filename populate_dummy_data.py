import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')

import django
django.setup()

from tasks.models import Task
from faker import Faker

fakegen = Faker()

def populate(N=5):

    for entry in range(N):

        # Create the fake data for that entry
        fake_desc = fakegen.text(max_nb_chars=200, ext_word_list=None)
        fake_date = fakegen.date()
        fake_name = fakegen.job()

        fake_task_data = Task.objects.get_or_create(name = fake_name, description = fake_desc, dateCreated = fake_date, dateUpdated = fake_date)[0]


if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete")
