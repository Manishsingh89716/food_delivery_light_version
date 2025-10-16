from django.shortcuts import render, redirect
from .models import User, Booking
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    if request.method == "POST":
        mobile = request.POST.get("mobile")
        otp = request.POST.get("otp")
        if otp != "1234":
            return redirect("/")
        user, _ = User.objects.get_or_create(mobile=mobile, defaults={"role":"customer"})
        if user.role == "customer":
            return redirect(f"/booking/customer/{user.id}/")
        elif user.role == "delivery":
            return redirect(f"/booking/delivery/{user.id}/")
        else:
            return redirect(f"/booking/admin/{user.id}/")
    return render(request, "login.html")

def customer_dashboard(request, user_id):
    user = User.objects.get(id=user_id)
    bookings = Booking.objects.filter(customer=user)
    return render(request, "customer.html", {"user": user, "bookings": bookings})

def create_booking(request, user_id):
    user = User.objects.get(id=user_id)
    Booking.objects.create(customer=user)
    return redirect(f"/booking/customer/{user_id}/")

def delivery_dashboard(request, user_id):
    user = User.objects.get(id=user_id)
    bookings = Booking.objects.filter(delivery=user)
    return render(request, "delivery.html", {"user": user, "bookings": bookings})

def update_status(request, booking_id):
    booking = Booking.objects.get(id=booking_id)
    booking.status = request.POST.get("status")
    booking.save()
    return redirect(f"/booking/delivery/{booking.delivery.id}/")

def admin_dashboard(request, user_id):
    bookings = Booking.objects.all()
    deliveries = User.objects.filter(role="delivery")
    return render(request, "admin.html", {"bookings": bookings, "deliveries": deliveries})

def assign_booking(request):
    booking_id = request.POST.get("booking_id")
    delivery_id = request.POST.get("delivery_id")
    booking = Booking.objects.get(id=booking_id)
    booking.delivery_id = delivery_id
    booking.save()
    return redirect(f"/booking/admin/1/")