import random, uuid, math
from django.contrib.auth.models import User


def get_random_ids(n):
    return random.sample(range(1, 21), n)


def get_answer_array(data, questions):
    answers = []
    for question in questions:
        answers += data.getlist(str(question))

    return [int(x) for x in answers]


def calculate_matching_result(creator_answers, friend_answers):
    match = [x for x in friend_answers if x in creator_answers]
    result = len(match) / len(creator_answers) * 100
    # result = round(result, 2)
    result = int(math.ceil(result))

    return result


def get_user(data):
    user = User.objects.filter(email=data.get('email'))
    if user:
        user = user.first()
    else:
        # Prepare data
        username = data.get('email').lower().split("@")[0] + "_" + uuid.uuid4().hex[:3]
        email = data.get('email').lower()
        password = 'Test123'
        name = data.get('full_name').split(' ')

        # Create User
        user = User.objects.create_user(username, email, password)
        user.first_name = name[0] if len(name) > 0 else ''
        user.last_name = name[1] if len(name) > 1 else ''
        user.save()

    return user
