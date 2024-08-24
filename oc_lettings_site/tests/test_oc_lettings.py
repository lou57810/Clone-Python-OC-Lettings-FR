import pytest
from django.test import TestCase
from django.urls import reverse


@pytest.mark.django_db  # Crée une database temporaire nulle en fin de test.
class HomePageTest(TestCase):
    """ Tests Endpoints """
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'home.html')
