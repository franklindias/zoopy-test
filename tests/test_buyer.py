import time
import unittest
from zoopy import buyer
from tests.base_unittest import BaseTest
from tests.resources import buyer_data_sample


class TestBuyer(BaseTest):
    def test_list_buyers(self):
        all_buyers = buyer.list()
        self.assertIsNotNone(all_buyers)

    def test_create_buyer(self):
        _buyer = buyer.create(params=buyer_data_sample.BUYER)
        self.assertIsNotNone(_buyer['id'])

    def test_details(self):
        _buyer = buyer.create(params=buyer_data_sample.BUYER)
        time.sleep(3)
        details = buyer.details(str(_buyer['id']))
        self.assertEqual(_buyer['id'], details['id'])

    def test_delete(self):
        _buyer = buyer.create(params=buyer_data_sample.BUYER)
        time.sleep(3)
        response = buyer.remove(buyer_id=str(_buyer['id']))
        self.assertTrue(response["deleted"])

if __name__ == '__main__':
    unittest.main()