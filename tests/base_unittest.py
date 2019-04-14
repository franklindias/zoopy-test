import unittest
from zoopy.utils import authentication_key


class BaseTest(unittest.TestCase):
    def setUp(self):
        authentication_key(
            api_key='zpk_test_ISLmKnlXiHGSsgjanvN6gbOJ', 
            marketplace_id="033ef887928e4fbb915276fa709993ed"
        )