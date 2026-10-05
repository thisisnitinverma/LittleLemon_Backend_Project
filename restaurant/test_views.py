from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import MenuItem, Booking
from restaurant.serializers import MenuItemSerializer


class MenuItemsViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = MenuItem.objects.create(title="Pizza", price=12.50, inventory=50)
        self.item2 = MenuItem.objects.create(title="Pasta", price=10.00, inventory=30)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class BookingsViewTest(TestCase):
    def setUp(self):
        self.booking1 = Booking.objects.create(
            first_name="Alice",
            reservation_date="2026-10-05",
            reservation_slot=15
        )

    def test_get_bookings_by_date(self):
        response = self.client.get('/restaurant/bookings?date=2026-10-05')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['first_name'], "Alice")