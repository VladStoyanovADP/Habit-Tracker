from django.test import TestCase
from .models import Person, Rewards
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
            "phone": "+51 513 897 6195",
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

    def test_get_users(self):
        '''
        Tests GET method
        '''
        Person.objects.create(**self.data)
        response = self.client.get(self.url)
        self.assertEqual(dict(response.data[0]), self.data)
        
    def test_post_users(self):
        '''
        Tests POST method
        '''
        data = self.data
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 1)
        self.assertEqual(Person.objects.get().name, "Nollie Oosthout de Vree")
        
    """
    TEST SUITE FOR /users/:user_id
    """
        
    def test_get_user_by_id(self):
        '''
        Tests GET method for fetching a user by id
        '''
        person = Person.objects.create(**self.data)
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
        person = Person.objects.create(**self.data)
        url = f"{self.url}{person.id}/"
        new_data = {"name": "New Name"}
        response = self.client.patch(url, new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        person.refresh_from_db()
        self.assertEqual(person.name, "New Name")
        
    def test_delete_user_by_id(self):
        '''
        Tests DELETE method
        '''
        person = Person.objects.create(**self.data)
        url = f"{self.url}{person.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Person.objects.count(), 0)
        
        
# class RewardsTestCase(APITestCase):
#     """
#     TEST SUITE FOR /users/:user_id/rewards
#     """
    
#     def setUp(self):
#         self.client = APIClient()
#         self.data1 = {
#             "name": "Nollie Oosthout de Vree",
#             "username": "noosthout0",
#             "password": "VR1I7KgnT8Mj",
#             "email": "noosthout0@stanford.edu",
#             "avatar_url": "https://robohash.org/quosillumearum.png?size=50x50&set=set1",
#             "description": "Universal 5th generation hub",
#             "created_at": "14/11/2019",
#             "currency": 58.13,
#             "phone": "+51 513 897 6195",
#         }
#         self.data2 = {
#             "user_id": 1,
#             "rewards_name": "extra snack",
#             "rewards_description": "have an extra snack after dinner",
#             "rewards_cost": 50
#         }
#         self.url = "users/{}/rewards"

#     def test_get_users_rewards_by_id(self):
#         '''
#         Tests GET method for fetching a user by id
#         '''
#         person = Person.objects.create(**self.data1)
#         data2 = self.data2.copy()
#         data2['user_id'] = person
#         Rewards.objects.create(**data2)
#         url = f"{self.url}{person.id}/rewards"
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data["rewards_name"], self.data2["rewards_name"])
#         self.assertEqual(
#             response.data["rewards_description"], self.data2["rewards_description"])
#         self.assertEqual(
#             response.data["rewards_cost"], self.data2["rewards_cost"])


#     def test_patch_users_reward(self):
#         '''
#         Tests PATCH method
#         '''
#         person = Person.objects.create(**self.data1)
#         rewards_data = {
#             "user_id": person,
#             "rewards_name": "extra snack",
#             "rewards_description": "have an extra snack after dinner",
#             "rewards_cost": 50
#         }
#         rewards = Rewards.objects.create(**rewards_data)
#         url = self.url.format(person.id)
#         new_data = {"rewards_name": "New Name"}
#         response = self.client.patch(url, new_data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         rewards.refresh_from_db()
#         self.assertEqual(rewards.rewards_name, "New Name")

#     def test_delete_users_reward(self):
#         '''
#         Tests DELETE method
#         '''
#         person = Person.objects.create(**self.data1)
#         self.data2 = {
#             "user_id": person.id,
#             "rewards_name": "extra snack",
#             "rewards_description": "have an extra snack after dinner",
#             "rewards_cost": 50
#         }
#         rewards = Rewards.objects.create(**self.data2)
#         url = f"{self.url}{person.id}/rewards"
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Person.objects.count(), 0)
