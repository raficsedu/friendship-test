from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, reverse
from .models import *
from .services import *
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from friendshiptest.settings import SITE_URL, NO_OF_ANS


# Create your views here.
def home(request):
    context = {'title': 'Home'}
    return render(request, 'friendship/home.html', context)


@login_required(login_url='new_friendship')
def my_friendship(request):
    my_friendships = FriendshipTest.objects.filter(user=request.user)
    context = {'title': 'My Friendship', 'my_friendships': my_friendships, 'url': SITE_URL}
    return render(request, 'friendship/my_friendship.html', context)


def new_friendship(request):
    # Get random ids and questions
    ids = get_random_ids(NO_OF_ANS)
    questions = Question.objects.filter(id__in=ids)

    # Comma separated ids
    ids = ','.join([str(x) for x in ids])

    context = {'title': 'New Friendship Test', 'questions': questions, 'ids': ids}
    return render(request, 'friendship/friendship.html', context)


def friendship_process(request):
    if request.method == 'POST':
        # Prepare data
        data = request.POST
        questions = data.get('questions').split(',')
        answers = get_answer_array(data, questions)

        # Get user
        user = get_user(data)
        login(request, user, backend='friendshiptest.auth.EmailBackend')

        # Save FriendshipTest
        friendship = FriendshipTest.objects.create(user=user, name=data.get('full_name', 'Test Name'))
        friendship.answers.set(answers)

        messages.success(request, 'Your friendship test created')
        return HttpResponseRedirect(reverse('my_friendship'))
    else:
        messages.error(request, 'Direct access not allowed')
        return HttpResponseRedirect(reverse('home'))


def friendship_test(request, code):
    friendship = FriendshipTest.objects.filter(code=code)
    if friendship:
        friendship = friendship.first()

        if request.method == 'POST':
            # Prepare data
            data = request.POST
            questions = data.get('questions').split(',')

            # Get creator answer
            creator_answers = list(friendship.answers.values_list('id', flat=True))

            # Get friend answer
            friend_answers = get_answer_array(data, questions)

            # Calculate matching result
            result = calculate_matching_result(creator_answers, friend_answers)

            context = {'title': 'Friendship Test Result', 'name': friendship.name, 'result': result}
            return render(request, 'friendship/friendship_result.html', context)

        # Get random ids and questions
        ids = list(set(friendship.answers.values_list('question_id', flat=True)))
        questions = Question.objects.filter(id__in=ids)

        # Comma separated ids
        ids = ','.join([str(x) for x in ids])

        context = {'title': 'Friendship Test', 'questions': questions, 'ids': ids, 'creator': friendship.name}
        return render(request, 'friendship/friendship_test.html', context)
    else:
        messages.error(request, 'Friendship test not found')
        return HttpResponseRedirect(reverse('home'))
