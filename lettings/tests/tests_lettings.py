import pytest
from django.test import TestCase
from django.contrib.auth.models import User
from lettings.models import Address, Letting


# Test logging:
@pytest.mark.django_db
class UserCreationTest(TestCase):

    def test_user_creation(self):
        User.objects.create_user(username='testuser', password='test123')
        self.assertTrue(User.objects.filter(username='testuser').exists())


# Test création d'une instance de l'adresse.
@pytest.mark.django_db
class AddressModelTestCase(TestCase):

    def test_address_creation(self):
        address = Address.objects.create(number=123, street='Test Street',
                                         city='Test City', state='TS', zip_code=12345, country_iso_code='TST')
        self.assertEqual(str(address), '123 Test Street')


# Test création d'une instance de Letting.
@pytest.mark.django_db
class LettingModelTestCase(TestCase):

    def test_letting_creation(self):
        address = Address.objects.create(number=123, street='Test Street',
                                         city='Test City', state='TS', zip_code=12345, country_iso_code='TST')
        letting = Letting.objects.create(title='Test Letting', address=address)
        self.assertEqual(str(letting), 'Test Letting')
