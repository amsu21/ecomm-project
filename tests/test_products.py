# from django.db import models
# from django.contrib.auth.models import Product

# import pytest

# def test_apply_discount():
#     product = Product("Test Product", 100.0)
#     discounted_price = product.apply_discount(10)
#     assert discounted_price == 90.0

# def test_apply_discount_invalid_percentage():
#     product = Product("Test Product", 100.0)
#     with pytest.raises(ValueError):
#         product.apply_discount(-5)