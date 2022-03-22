from django.test import TestCase
import random
from friendship.models import *
from friendship.services import get_random_ids, calculate_matching_result
from friendshiptest.settings import NO_OF_ANS


class CalculateResultTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        no_of_q = 20
        for q in range(1, no_of_q + 1):
            q_type = random.randint(1, 2)
            question = Question.objects.create(title='Dummy question - ' + str(q), type=q_type)

            no_of_a = random.randint(3, 5)
            for a in range(1, no_of_a + 1):
                Answer.objects.create(question=question, answer='Dummy Answer - ' + str(a))

    def setUp(self):
        username = 'raficsedu'
        email = 'raficsedu@gmail.com'
        password = 'Test123'
        name = 'Muntasir Rahman'.split(' ')

        # Create User
        self.user = User.objects.create_user(username, email, password)
        self.user.first_name = name[0] if len(name) > 0 else ''
        self.user.last_name = name[1] if len(name) > 1 else ''
        self.user.save()

        # Get random question
        ids = get_random_ids(NO_OF_ANS)
        self.questions = Question.objects.filter(id__in=ids)

        # Prepare user answer
        self.answers = []
        for q in self.questions:
            self.answers.append(q.answers.first().id)

        # Insert FriendshipTest
        self.friendship_test = FriendshipTest.objects.create(user=self.user, name='Test Name')
        self.friendship_test.answers.set(self.answers)

    def test_friend_result_calculation(self):
        self.answers_1 = []
        self.answers_2 = []
        self.answers_3 = []

        # Prepare friend answer
        c = 1
        for q in self.questions:
            self.answers_1.append(q.answers.first().id)  # 100%
            self.answers_2.append(q.answers.last().id)  # 0%
            if c % 2 == 0:
                self.answers_3.append(q.answers.first().id)  # 50%
            else:
                self.answers_3.append(q.answers.last().id)  # 50%

            c += 1

        # Prepare result
        result_1 = calculate_matching_result(self.answers, self.answers_1)
        result_2 = calculate_matching_result(self.answers, self.answers_2)
        result_3 = calculate_matching_result(self.answers, self.answers_3)

        # Compare with expected
        self.assertEqual(result_1, 100)
        self.assertEqual(result_2, 0)
        self.assertEqual(result_3, 50)
