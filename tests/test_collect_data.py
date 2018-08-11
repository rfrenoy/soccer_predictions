import unittest
from soccer_predictions.collect_data import clean_year_format


class TestCollectData(unittest.TestCase):
    def test_clean_year_format_should_raise_if_input_is_text_and_has_length_different_than_two_or_four(self):
        # Given
        incorrect_date = '200'

        # Then
        with self.assertRaises(ValueError):
            # When
            clean_year_format(incorrect_date)

    def test_clean_year_format_should_raise_if_input_is_int_and_has_length_different_than_two_or_four(self):
        # Given
        incorrect_date = 200

        # Then
        with self.assertRaises(ValueError):
            # When
            clean_year_format(incorrect_date)

    def test_clean_year_format_should_return_string(self):
        # Given
        numeric_input = 2001
        text_input = '2001'

        # When
        out1 = clean_year_format(numeric_input)
        out2 = clean_year_format(text_input)

        # Then
        self.assertTrue(type(out1) is str)
        self.assertTrue(type(out2) is str)

    def test_clean_year_format_should_return_year_in_two_digit_format_when_input_is_two_or_four_digits_long(self):
        # Given
        numeric_input = 01
        text_input = 2001

        # When
        out1 = clean_year_format(numeric_input)
        out2 = clean_year_format(text_input)

        # Then
        self.assertEqual(out1, '01')
        self.assertEqual(out2, '01')
