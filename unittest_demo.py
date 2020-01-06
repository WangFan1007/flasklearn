import unittest
from login import app
import json


class LoginDemo(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.client = app.test_client()

    def test_empty_all(self):

        resp = self.client.post('/login', data={})
        ret = json.loads(resp.data)
        self.assertIn('code', ret)
        self.assertEqual(ret['code'], 1)

    def test_empty_username(self):

        resp = self.client.post('/login', data={"password": "python"})
        ret = json.loads(resp.data)
        self.assertIn('code', ret)
        self.assertEqual(ret['code'], 1)

    def test_empty_password(self):

        resp = self.client.post('/login', data={"user_name": "admin"})
        ret = json.loads(resp.data)
        self.assertIn('code', ret)
        self.assertEqual(ret['code'], 1)

    def test_wrong(self):

        resp = self.client.post(
            '/login', data={"user_name": "admin", "password": "123"})
        ret = json.loads(resp.data)
        self.assertIn('code', ret)
        self.assertEqual(ret['code'], 2)

    def test_right(self):

        resp = self.client.post(
            '/login', data={"user_name": "admin", "password": "python"})
        ret = json.loads(resp.data)
        self.assertIn('code', ret)
        self.assertEqual(ret['code'], 0)


def num_dev(num1, num2):
    assert isinstance(num1, int)
    assert isinstance(num2, int)
    assert num2 != 0
    print(num1/num2)


if __name__ == '__main__':
    # num_dev(100, 0)
    unittest.main()
