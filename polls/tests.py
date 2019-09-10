from django.test import TestCase


# Create your tests here.
class DemoTestCase(TestCase):
    def test_add_two_number_valid(self):
        a = 10
        b = 20
        c = a + b
        self.assertEqual(c, 30)

    # def test_add_two_number_invalid(self):
    #     a = 10
    #     b = 20
    #     c = a + b
    #     self.assertEqual(c, 40)
