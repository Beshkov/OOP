import unittest

from skeleton.project.player.beginner import Beginner


class TestBeginner(unittest.TestCase):
    def setUp(self):
        self.p = Beginner('New_player')

    def test_set_up(self):
        self.assertEqual(self.p.health, 50)
        self.assertEqual(self.p.username, 'New_player')
        self.assertEqual(self.p.is_dead, False)

    def test_name_if_name_is_passed_as_empty_should_give_error(self):
        with self.assertRaises(Exception) as error:
            self.p.username = ''

        self.assertEqual('Player\'s username cannot be an empty string. ', str(error.exception))

    def test_health_if_set_bellow_zero(self):
        with self.assertRaises(ValueError) as cm:
            self.p.health = -1

        self.assertEqual("Player's health bonus cannot be less than zero. ", cm.exception.__str__())

    def test__take_dame_method_if_it_take_player_hp_to_0_or_bellow_0(self):
        damage_1 = 50
        damage_2 = 60
        self.p.take_damage(damage_1)
        self.assertEqual(0, self.p.health)
        self.assertEqual(True, self.p.is_dead)
        self.p.health = 50
        with self.assertRaises(ValueError) as cm:
            self.p.take_damage(damage_2)
        self.assertEqual('Player\'s health bonus cannot be less than zero. ', str(cm.exception))

if __name__ == '__main__':
    unittest.main()
