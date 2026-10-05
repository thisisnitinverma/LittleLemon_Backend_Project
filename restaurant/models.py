from django.db import models


class Booking(models.Model):
    first_name = models.CharField(max_length=255)
    reservation_date = models.DateField()
    reservation_slot = models.IntegerField(default=10)

    class Meta:
        unique_together = ('reservation_date', 'reservation_slot')

    def __str__(self) -> str:
        return f"{self.first_name} : {self.reservation_date} @ {self.reservation_slot}:00"


class MenuItem(models.Model):
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.SmallIntegerField()

    def __str__(self) -> str:
        return f"{self.title} : {self.price}"