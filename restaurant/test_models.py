from django.test import TestCase
from restaurant.models import MenuItem, Booking


class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(str(item), "IceCream : 80")


class BookingTest(TestCase):
    def test_booking_str(self):
        booking = Booking.objects.create(
            first_name="John",
            reservation_date="2026-10-05",
            reservation_slot=12
        )
        self.assertEqual(str(booking), "John : 2026-10-05 @ 12:00")