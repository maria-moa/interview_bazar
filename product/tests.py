from django.test import TestCase
from django.utils import dateparse
from freezegun import freeze_time
from rest_framework.test import APIClient

from .factories import ProductFactory


class ProductCRUDTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.f_time_str = "2023-10-09T13:11:44.657109Z"
        cls.f_datetime = dateparse.parse_datetime(cls.f_time_str)

        with freeze_time(cls.f_time_str):
            cls.product_1 = ProductFactory.create()
            cls.product_2 = ProductFactory.create()

    def setUp(self):
        self.client = APIClient()

    def test_get_products(self):

        expected_response = {
            "count": 2,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.product_2.id,
                    "name": self.product_2.name,
                    "created_at": self.f_time_str,
                    "updated_at": self.f_time_str,
                },
                {
                    "id": self.product_1.id,
                    "name": self.product_1.name,
                    "created_at": self.f_time_str,
                    "updated_at": self.f_time_str,
                },
            ],
        }

        response = self.client.get("/api/v1/products/")
        self.assertEqual(response.status_code, 200)
        self.maxDiff = None
        self.assertEqual(response.json(), expected_response)

    def test_creat_product(self):
        response = self.client.post("/api/v1/products/")
        self.assertEqual(response.status_code, 401)

    def test_detail_product(self):

        response = self.client.get("/api/v1/products/{}".format(self.product_1.id))
        expected_response = {
            "id": self.product_1.id,
            "name": self.product_1.name,
            "created_at": self.f_time_str,
            "updated_at": self.f_time_str,
        }

        self.assertEqual(response.status_code, 200)
        self.maxDiff = None
        self.assertEqual(response.json(), expected_response)
