import unittest
import main.py

class FlaskTestCase(unittest.TestCase):

    def setUp(self):
        main.app.testing = True
        client = main.app.test_client()
        rv = client.get('/?dice=振る')
        self.html = rv.data.decode('utf-8').lower()

    def test_result(self):
        self.assertTrue('dice_' in self.html, msg='結果が正しく表示されていません')
