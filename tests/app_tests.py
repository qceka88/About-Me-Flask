import unittest

from app import app


class TestIndexView(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_view(self):
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<!DOCTYPE html>', response.data)


class TestBotResponseView(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_bot_response_view(self):
        message = "Hello"
        response = self.app.get(f"/get?message={message}")
        self.assertEqual(response.status_code, 200)
