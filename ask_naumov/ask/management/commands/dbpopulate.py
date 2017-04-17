from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from django.conf import settings
from django.core.files import File
from ask.models import Answer, Question, Tag, Profile
import random, os

class Command(BaseCommand):
    help = 'Populate db'

    def handle(self, *args, **options):
        users = [User.objects.create_user('user'+str(i), str(i)+'@.com', 'pass'+str(i)) for i in range(20)]
        
        profiles = list()
        for i in range(len(users)):
            avaname = 'avatar1.jpg' if random.choice([True, False]) else 'avatar2.jpg'
            ava = open(os.path.join(settings.MEDIA_ROOT, avaname), 'rb')
            profile = Profile.objects.create(user=users[i], rating=random.randint(1,5))
            profile.avatar.save('av'+str(i)+'.jpg', File(ava))
            profile.save()
            profiles.append(profile)
            ava.close()
        
        tags = { i : Tag.objects.create(content='tag'+str(i)) for i in range(2,9) }
        
        for i in range(1, 150):
            q = Question.objects.create(title='title'+str(i), content='text'+str(i), rating=random.randint(1,5),
                                       author=random.choice(profiles))
            for k,v in tags.items():
                if i % k == 0: 
                    q.tags.add(v)
            for j in range(1, random.randint(1,150)): 
                q.answer_set.create(content='text'+str(j), rating=random.randint(1,5), is_correct=random.choice([True, False]))
            q.save()
        
        self.stdout.write(self.style.SUCCESS('DB successfully populated'))
