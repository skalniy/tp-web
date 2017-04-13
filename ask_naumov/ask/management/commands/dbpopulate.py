from django.core.management.base import BaseCommand, CommandError
from ask.models import Answer, Question, Tag
import random

class Command(BaseCommand):
    help = 'Populate db'

    def handle(self, *args, **options):
        tags = { i : Tag.objects.create(content='tag'+str(i)) for i in range(2,9) }
        
        for i in range(1, 150):
            q = Question.objects.create(title='title'+str(i), content='text'+str(i), rating=random.randint(1,5))
            for k,v in tags.items():
                if i % k == 0: 
                    q.tags.add(v)
            for j in range(1, random.randint(1,150)): 
                q.answer_set.create(content='text'+str(j), rating=random.randint(1,5), is_correct=random.choice([True, False]))
            q.save()
        
        self.stdout.write(self.style.SUCCESS('DB successfully populated'))
