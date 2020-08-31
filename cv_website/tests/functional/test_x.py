from django.test import TestCase

class MockTest(TestCase):
    def test_base(self):
        print("I ran")
        assert True == False