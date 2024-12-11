from django.test import TestCase

# Create your tests here.from django.test import TestCase
from django.contrib.auth.models import User
from ecom.models import Customer, Product, Orders, Feedback

class CustomerModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", first_name="John", last_name="Doe", password="password123")
        self.customer = Customer.objects.create(
            user=self.user,
            address="123 Test St",
            mobile="1234567890"
        )

    def test_customer_creation(self):
        self.assertEqual(self.customer.user.username, "testuser")
        self.assertEqual(self.customer.get_name, "John Doe")
        self.assertEqual(self.customer.get_id, self.user.id)

    def test_customer_str_representation(self):
        self.assertEqual(str(self.customer), "John")

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name="Laptop",
            price=1200,
            description="A high-quality laptop"
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, "Laptop")
        self.assertEqual(self.product.price, 1200)
        self.assertEqual(self.product.description, "A high-quality laptop")

    def test_product_str_representation(self):
        self.assertEqual(str(self.product), "Laptop")

class OrdersModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", first_name="John", last_name="Doe", password="password123")
        self.customer = Customer.objects.create(
            user=self.user,
            address="123 Test St",
            mobile="1234567890"
        )
        self.product = Product.objects.create(
            name="Laptop",
            price=1200,
            description="A high-quality laptop"
        )
        self.order = Orders.objects.create(
            customer=self.customer,
            product=self.product,
            email="customer@example.com",
            address="123 Test St",
            mobile="1234567890",
            status="Pending"
        )

    def test_order_creation(self):
        self.assertEqual(self.order.customer, self.customer)
        self.assertEqual(self.order.product, self.product)
        self.assertEqual(self.order.email, "customer@example.com")
        self.assertEqual(self.order.status, "Pending")

class FeedbackModelTest(TestCase):
    def setUp(self):
        self.feedback = Feedback.objects.create(
            name="John Doe",
            feedback="Great service!"
        )

    def test_feedback_creation(self):
        self.assertEqual(self.feedback.name, "John Doe")
        self.assertEqual(self.feedback.feedback, "Great service!")

    def test_feedback_str_representation(self):
        self.assertEqual(str(self.feedback), "John Doe")