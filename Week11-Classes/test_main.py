from unittest import TestCase

from main import Chair


class TestChair(TestCase):

    def test_chair_init(self):
        # arrange
        expected_current_height = 10
        expected_min_height = 10
        expected_max_height = 50
        expected_arms = 2

        # act
        chair = Chair(expected_min_height, expected_max_height, expected_arms)
        actual_height = chair.get_height_in_cm()
        actual_min = chair.get_minimum_height_in_cm()
        actual_max = chair.get_maximum_height_in_cm()
        actual_arms = chair.get_number_of_arms()

        # assert
        self.assertEqual(expected_arms, actual_arms)
        self.assertEqual(expected_max_height, actual_max)
        self.assertEqual(expected_min_height, actual_min)
        self.assertEqual(expected_current_height, actual_height)

    def test_change_height(self):
        # AAA

        # Arrange - setup everything we need to test
        expected_height = 25
        chair = Chair(10, 50, 2)


        # Act - calling the code we want to test
        chair.change_height(15)
        actual_height = chair.get_height_in_cm()


        # Assert - did I get what I expected?
        self.assertEqual(expected_height, actual_height)

    def test_change_height_stops_at_min(self):
        # AAA

        # Arrange - setup everything we need to test
        expected_height = 10
        chair = Chair(10, 50, 2)


        # Act - calling the code we want to test
        chair.change_height(-15)
        actual_height = chair.get_height_in_cm()


        # Assert - did I get what I expected?
        self.assertEqual(expected_height, actual_height)

    def test_change_height_stops_at_max(self):
        # AAA

        # Arrange - setup everything we need to test
        expected_height = 50
        chair = Chair(10, 50, 2)


        # Act - calling the code we want to test
        chair.change_height(100)
        actual_height = chair.get_height_in_cm()


        # Assert - did I get what I expected?
        self.assertEqual(expected_height, actual_height)

    def test_set_minimum_height_in_cm_doesnt_go_below_zero(self):
        # Arrange
        expected_min = 10
        chair = Chair(10, 50, 2)

        # Act - https://stackoverflow.com/questions/3877134/testing-in-python-how-can-i-use-assertraises-in-testing-using-unittest
        # type of exception, function to call, argument to provide
        self.assertRaises(ValueError, chair.set_minimum_height_in_cm, -10)
        actual_min = chair.get_minimum_height_in_cm()

        # Assert
        self.assertEqual(expected_min, actual_min)

    def test_set_minimum_height_in_cm_doesnt_go_above_max(self):
        # Arrange
        expected_min = 10
        chair = Chair(10, 50, 2)

        # Act
        self.assertRaises(ValueError, chair.set_minimum_height_in_cm, 100)
        actual_min = chair.get_minimum_height_in_cm()

        # Assert
        self.assertEqual(expected_min, actual_min)

    def test_set_minimum_height_above_current_raises_exception(self):
        # Arrange
        expected_current = 10
        chair = Chair(10, 50, 2)

        # Act
        self.assertRaises(ValueError, chair.set_minimum_height_in_cm, 25)
        actual_height = chair.get_height_in_cm()

        # Assert
        self.assertEqual(expected_current, actual_height)


    def test_chair_str(self):
        # Arrange
        expected_str = "grey chair currently at 10 cm"
        chair = Chair(10, 50, 2)
        chair.color = 'grey'

        # Act
        actual_str = str(chair)

        # Assert
        self.assertEqual(expected_str, actual_str)