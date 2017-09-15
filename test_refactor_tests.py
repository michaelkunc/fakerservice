import unittest
from app import create_app


class StatusTest(unittest.TestCase):

    test_map = {
        'addresses': '/addresses/full_addresses/',
        'countries': '/addresses/countries/'
    }

    def test_status_code(self):
        """
        Test that endpoints return 200s
        """
        for name, url in self.test_map.items():
            self.app = create_app(config_name='testing')
            self.client = self.app.test_client
            url = self.client().get(url)
            with self.subTest(name=name):
                self.assertEqual(url.status_code, 200, name)

if __name__ == '__main__':
    unittest.main()
