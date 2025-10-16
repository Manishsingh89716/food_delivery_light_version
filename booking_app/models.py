from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, blank=True)
    mobile = models.CharField(max_length=15, unique=True)
    role = models.CharField(max_length=20, choices=[("customer","Customer"),("delivery","Delivery"),("admin","Admin")])

    def __str__(self):
        return f"{self.mobile} ({self.role})"

class Booking(models.Model):
    customer = models.ForeignKey(User, related_name="customer_bookings", on_delete=models.CASCADE)
    delivery = models.ForeignKey(User, related_name="delivery_bookings", on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=20, default="Pending")  # Pending, Start, Reached, Collected, Delivered

    def __str__(self):
        return f"Booking {self.id} - {self.status}"

class ChatMessage(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    sender = models.CharField(max_length=20)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
