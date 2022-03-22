import random
import django
import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "friendshiptest.settings")
sys.path.append(os.path.join(os.path.realpath(os.path.dirname(__file__)), "..", ".."))
django.setup()

from friendship.models import Question, Answer
from django.core import management

# Migrate
management.call_command("migrate", no_input=True)

# Seed
no_of_q = 20
for q in range(1, no_of_q+1):
    q_type = random.randint(1, 2)
    question = Question.objects.create(title='Dummy question - ' + str(q), type=q_type)

    no_of_a = random.randint(3, 5)
    for a in range(1, no_of_a+1):
        Answer.objects.create(question=question, answer='Dummy Answer - ' + str(a))
