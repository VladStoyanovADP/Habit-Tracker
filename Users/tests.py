from django.test import TestCase
from .models import Person, Rewards
from Achievements.models import Achievements
from rest_framework.test import APIClient
from rest_framework.test import APITestCase
from rest_framework import status
from collections import OrderedDict

# Create your tests here.


class UsersTestCase(APITestCase):

    """
    TEST SUITE FOR /users/
    """

    def setUp(self):
        self.client = APIClient()
        self.data = {
            "name": "Nollie Oosthout de Vree",
            "username": "noosthout0",
            "password": "VR1I7KgnT8Mj",
            "email": "noosthout0@stanford.edu",
            "avatar_url": "https://robohash.org/quosillumearum.png?size=50x50&set=set1",
            "description": "Universal 5th generation hub",
            "created_at": "14/11/2019",
            "currency": "58.13",
            "phone": "+51 513 897 6195"
        }
        self.data2 = {
            "achievement_name": "1 day streak",
            "achievement_img_url": "www.needtofindimage.co.uk",
            "achievement_description": "One day, right one! ",
            "achievement_reward": "5.0"
        }
        self.url = "/users/"

    def test_list_users(self):
        '''
        Test the status
        '''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_properties(self):
        '''
        Test whether each user has an name, username, password, email, avatar_url, description, created_at,
        currency, and phone properties
        '''
        properties = ["name", "username", "password", "email",
                      "avatar_url", "description", "created_at", "currency", "phone"]

        for prop in properties:
            self.assertIn(prop, self.data.keys())

    def test_post_users(self):
        '''
        Tests POST method
        '''
        achievement = Achievements.objects.create(**self.data2)
        person = Person.objects.create(**self.data)
        person.achievements.add(achievement)
        person_dict = {
            "name": person.name,
            "username": person.username,
            "password": person.password,
            "email": person.email,
            "avatar_url": person.avatar_url,
            "description": person.description,
            "created_at": person.created_at,
            "currency": person.currency,
            "phone": person.phone,
            'achievements': [a.id for a in person.achievements.all()]
        }
        response = self.client.post(self.url, person_dict, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    """
    TEST SUITE FOR /users/:user_id
    """

    def test_get_user_by_id(self):
        '''
        Tests GET method for fetching a user by id
        '''
        achievement = Achievements.objects.create(**self.data2)
        person = Person.objects.create(**self.data)
        person.achievements.add(achievement)
        url = f"{self.url}{person.id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], self.data["name"])
        self.assertEqual(response.data["username"], self.data["username"])
        self.assertEqual(response.data["email"], self.data["email"])

    def test_patch_users(self):
        '''
        Tests PATCH method
        '''
        achievement = Achievements.objects.create(**self.data2)
        person = Person.objects.create(**self.data)
        person.achievements.add(achievement)
        url = f"{self.url}{person.id}/"
        new_data = {"name": "New Name"}
        response = self.client.patch(url, new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        person.refresh_from_db()
        print(person)
        self.assertEqual(person.name, "New Name")

    def test_delete_user_by_id(self):
        '''
        Tests DELETE method
        '''
        achievement = Achievements.objects.create(**self.data2)
        person = Person.objects.create(**self.data)
        url = f"{self.url}{person.id}/"
        person.achievements.add(achievement)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 0)


class RewardsTestCase(APITestCase):
    """
    TEST SUITE FOR /users/:user_id/rewards
    """

    def setUp(self):
        self.client = APIClient()
        self.person_data = {
            "name": "Nollie Oosthout de Vree",
            "username": "noosthout0",
            "password": "VR1I7KgnT8Mj",
            "email": "noosthout0@stanford.edu",
            "avatar_url": "https://robohash.org/quosillumearum.png?size=50x50&set=set1",
            "description": "Universal 5th generation hub",
            "created_at": "14/11/2019",
            "currency": "58.13",
            "phone": "+51 513 897 6195",
        }
        self.person = Person.objects.create(**self.person_data)

        self.rewards_data = {
            "user_id": self.person,
            "rewards_name": "extra snack",
            "rewards_description": "have an extra snack after dinner",
            "rewards_cost": "50"
        }
        self.rewards = Rewards.objects.create(**self.rewards_data)
        self.url = f"/users/{self.person.id}/rewards"

    def test_get_users_rewards_by_id(self):
        '''
        Tests GET method for fetching a user by id
        '''
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["user_id"], self.person.id)
