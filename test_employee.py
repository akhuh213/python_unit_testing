import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Test for Employee Class"""

    def test_email(self):
        levin = Employee('levin', 'batallones', 2000000)
        martin = Employee('martin', 'briceno', 199999)

        self.assertEqual(levin.email, 'levin.batallones@sei713.com')
        self.assertEqual(martin.email, 'martin.briceno@sei713.com')

    def test_fullname(self):
        rome = Employee('Rome', 'Bell', 100000)
        adam = Employee('Adam', 'Honroe', 20000)

        self.assertEqual(rome.fullname, 'Rome Bell')
        self.assertEqual(adam.fullname)

if __name__=='__main__':
    unittest.main()