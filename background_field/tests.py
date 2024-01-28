from django.test import TestCase
from django.utils import dateparse
from freezegun import freeze_time
from rest_framework.test import APIClient

from product.factories import ProductFactory
from service.factories import ServiceFactory
from user.factories import UserFactory
from whole_sale.factories import WholeSaleFactory


class ProductCRUDTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.f_time_str = "2023-10-09T13:11:44.657109Z"
        cls.f_datetime = dateparse.parse_datetime(cls.f_time_str)

        with freeze_time(cls.f_time_str):
            cls.user = UserFactory.create()
            cls.product_1 = ProductFactory.create()
            cls.product_2 = ProductFactory.create()
            cls.service_1 = ServiceFactory.create()
            cls.service_2 = ServiceFactory.create()
            cls.wholesale_1 = WholeSaleFactory.create()
            cls.wholesale_2 = WholeSaleFactory.create()

    def setUp(self):
        self.client = APIClient()

    def test_crud_background_field(self):
        self.client.force_authenticate(user=self.user)

        with freeze_time(self.f_time_str):
            response_post = self.client.post(
                "/api/v1/background_field/",
                {
                    "producer": [self.product_1.id, self.product_2.id],
                    "whole_sale": [self.wholesale_1.id],
                    "service": [self.service_2.id],
                },
            )
        self.assertEqual(response_post.status_code, 201)

        expected_response_post = {
            "producer": [self.product_2.id, self.product_1.id],
            "whole_sale": [self.wholesale_1.id],
            "service": [self.service_2.id],
            "created_at": self.f_time_str,
            "updated_at": self.f_time_str,
        }

        response_dict_post = response_post.json()
        self.assertIn("id", response_dict_post)
        id = response_dict_post.pop("id")

        self.maxDiff = None
        self.assertEqual(response_dict_post, expected_response_post)

        expected_response_get = {
            "id": id,
            "producer": [
                {
                    "id": self.product_2.id,
                    "created_at": self.f_time_str,
                    "updated_at": self.f_time_str,
                    "name": self.product_2.name,
                },
                {
                    "id": self.product_1.id,
                    "created_at": self.f_time_str,
                    "updated_at": self.f_time_str,
                    "name": self.product_1.name,
                },
            ],
            "whole_sale": [
                {
                    "id": self.wholesale_1.id,
                    "created_at": self.f_time_str,
                    "updated_at": self.f_time_str,
                    "name": self.wholesale_1.name,
                }
            ],
            "service": [
                {
                    "id": self.service_2.id,
                    "created_at": self.f_time_str,
                    "updated_at": self.f_time_str,
                    "name": self.service_2.name,
                }
            ],
            "created_at": self.f_time_str,
            "updated_at": self.f_time_str,
        }
        response_get = self.client.get("/api/v1/background_field/mine")
        self.assertEqual(response_get.status_code, 200)
        self.maxDiff = None
        self.assertEqual(response_get.json(), expected_response_get)

        response_gey_by_id = self.client.get("/api/v1/background_field/{}".format(id))
        self.assertEqual(response_gey_by_id.status_code, 200)
        self.maxDiff = None
        self.assertEqual(response_gey_by_id.json(), expected_response_get)

        with freeze_time(self.f_time_str):
            response_put = self.client.put(
                "/api/v1/background_field/{}".format(id),
                {"producer": [self.product_1.id], "whole_sale": [self.wholesale_2.id], "service": [self.service_1.id]},
            )

        self.assertEqual(response_put.status_code, 200, msg=response_put.json())

        expected_response_put = {
            "id": id,
            "producer": [self.product_1.id],
            "whole_sale": [self.wholesale_2.id],
            "service": [self.service_1.id],
            "created_at": self.f_time_str,
            "updated_at": self.f_time_str,
        }

        self.maxDiff = None
        self.assertEqual(response_put.json(), expected_response_put)

        response_delete = self.client.delete("/api/v1/background_field/{}".format(id))
        self.assertEqual(response_delete.status_code, 204)
