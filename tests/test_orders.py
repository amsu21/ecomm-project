# from django.db import models
# from django.contrib.auth.models import Orders, Prodcut, User

# from ecom.models import Product


# def test_order_creation():
#     user = User("john_doe", "john@example.com")
#     product1 = Product("Laptop", 1200.00, 10)
#     product2 = Product("Mouse", 25.00, 50)
#     order = Orders(user, [product1, product2])

#     assert order.user == user
#     assert len(order.products) == 2
#     assert order.status == "Pending"

# def test_order_completion():
#     user = User("john_doe", "john@example.com")
#     product = Product("Laptop", 1200.00, 10)
#     order = Orders(user, [product])
#     order.complete_order()

#     assert order.status == "Completed"