import unittest

from project.survivor import Survivor

class TestSurvivor(unittest.TestCase):

    def setUp(self):
        self.s = Survivor('Alex', 20)

    def test__setup_if_all_is_valid(self):
        self.assertEqual('Alex', self.s.name)
        self.assertEqual(20, self.s.age)
        self.assertEqual(100, self.s.health)
        self.assertEqual(100, self.s.needs)

    def test__if_name_is_empty_str_expect_value_error_with_ms(self):

        with self.assertRaises(ValueError) as message:
            self.s.name = ''
        self.assertEqual('Name not valid!', str(message.exception))

    def test__if_age_is_set_bellow_0_expect_value_error_with_ms(self):

        with self.assertRaises(ValueError) as message:
            self.s.age = -1
        self.assertEqual('Age not valid!', str(message.exception))

    def test__if_health_is_set_bellow_0_expect_value_error_with_ms(self):
        with self.assertRaises(ValueError) as message:
            self.s.health = -1
        self.assertEqual('Health not valid!', str(message.exception))

    def test_if_needs_is_set_bellow_0__expect_value_error_with_ms(self):
        with self.assertRaises(ValueError) as message:
            self.s.needs = -1
        self.assertEqual('Needs not valid!', str(message.exception))

    def test_needs_sustenance_if_health_at_100(self):
        self.assertEqual(False, self.s.needs_sustenance)

    def test_needs_sustenance_if_health_bellow_100(self):
        self.s.needs = 90
        self.assertEqual(True, self.s.needs_sustenance)

    def test_needs_healing_if_health_at_100(self):
        self.assertEqual(False, self.s.needs_healing)

    def test_needs_healing_if_health_bellow_100(self):
        self.s.health = 90
        self.assertEqual(True, self.s.needs_healing)

if __name__ == "__main__":
    unittest.main()