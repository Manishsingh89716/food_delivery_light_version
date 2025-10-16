# 🍽️ Food Delivery App (with Real-time Chat using Django Channels)

This is a simple **Food Delivery Web App** built with **Django + Channels (WebSocket)** that allows real-time chat communication between the customer and restaurant.

---
## 🚀 Features

- Customer can book a food order.
- Each booking page includes a **real-time chat** between the customer and restaurant.
- **WebSocket** powered live messaging using **Django Channels**.
- Uses **Daphne** as ASGI server.
- SQLite database for simplicity.

---

## 🏗️ Tech Stack

| Component | Technology Used |
|------------|----------------|
| Backend | Django 5 + Channels |
| Frontend | HTML, CSS, JavaScript |
| WebSocket Server | Daphne |
| Database | SQLite3 |
| Channel Layer | In-memory (no Redis required) |

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
- git clone https://github.com/manishsingh89716/food_delivery_light_version.git
- cd food_delivery_app

- python -m venv venv
- venv\Scripts\activate       # On Windows
- source venv/bin/activate    # On Linux/Mac

---
## Install Dependencies

- pip install -r requirements.txt

---

## Run Migrations

- python manage.py makemigrations
- python manage.py migrate

---

## Run Server (with Daphne)

- daphne -p 8000 food_delivery_app.asgi:application

---

## 💬 Chat Flow Example

- Open /booking/customer/<id>/ in the browser.
- You’ll see a chat window to send messages.
- When you send a message, it’s broadcast live using WebSockets.
- Another connected user (like restaurant staff) will receive it instantly.
