<h1>🛒 E-commerce API with Django REST Framework</h1>
This API is built using Django REST Framework and powers the backend of an e-commerce app. It handles everything needed for a typical online store, such as managing products, customers, orders, and authentication.

🔧 Core Features
User Authentication

Signup, Login, Logout

JWT or Token-based authentication

User roles: Customer & Admin

Products

List all products

View product details

Search and filter by category, price, etc.

Categories

Organize products by categories

Admins can create, update, and delete categories

Cart

Add/remove products to cart

Update quantity

View current cart

Orders

Create orders from cart

View past orders

Order status tracking (Pending, Shipped, Delivered)

Payments (Optional)

Integrate payment gateways (like Stripe, PayPal)

Admin Panel

Manage users, products, categories, and orders via Django admin or API

🔒 Security
Token-based authentication with permissions and throttling

Input validation and error handling

🚀 Technologies Used
Django

Django REST Framework (DRF)

SQLite

JWT Authentication (using djangorestframework-simplejwt)

