import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','course_project.settings')


import django
django.setup()

##FAKE POP SCRIPT

import random
from course_app.models import AccessRecord,Webpage,Topic
from faker import Faker

fakegen= Faker()
topics=['Search','SocialMedia','Marketplace','Games','News']


def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]  #it returns a tuple and inorder to get just one reference value [0] is used
        #this-"-------------------" reflects the name if already available else creates one
    t.save()
    return t
    #similar commands which we've used using shell


def populate(N=5):

    for entry in range(N):

        #get the topic for the entry
        top = add_topic()

        # create fake data for that entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        #create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

        # create fake access record for that webpage
        acc_rec= AccessRecord.objects.get_or_create(name=webpg,date=fake_date)


if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
