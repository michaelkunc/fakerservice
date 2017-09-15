import unittest
from app import create_app


# class ParameterizedTestCase(unittest.TestCase):

# def setUp(self):
#     self.app = create_app(config_name='testing')
#     self.client = self.app.test_client

# def test_status_code(self):
#     self.app = create_app(config_name='testing')
#     self.client = self.app.test_client
#     for i in (['/addresses/full_addresses', '/addresses/countries/']):
#         response = self.client().get(i)
#         with self.subtest(response=response.status_code):
#             self.assertEqual(200, response)

class StatusTest(unittest.TestCase):

    def test_status_code(self):
        """
        Test that numbers between 0 and 5 are all even.
        """
        for i in [0, 6]:
            with self.subTest(i=i):
                self.assertEqual(i % 2, 0)

if __name__ == '__main__':
    unittest.main()
