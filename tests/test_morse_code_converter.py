import unittest
from app.morse_code_converter import convert_text


class TestConvertText(unittest.TestCase):
    def test_single_letter_conversion(self):
        self.assertEqual(convert_text('A'), '.-')
        self.assertEqual(convert_text('Z'), '--..')
        self.assertEqual(convert_text('7'), '--...')

    def test_word_conversion(self):
        self.assertEqual(convert_text('HELLO'), '.... . .-.. .-.. ---')
        self.assertEqual(convert_text('WORLD'), '.-- --- .-. .-.. -..')

    def test_sentence_conversion(self):
        self.assertEqual(convert_text('HELLO WORLD'),
                         '.... . .-.. .-.. ---         .-- --- .-. .-.. -..')
        self.assertEqual(convert_text('THIS IS A TEST'),
                         '- .... .. ...         .. ...         .-         - . ... -')

    def test_mixed_case_conversion(self):
        self.assertEqual(convert_text('Hello World'),
                         '.... . .-.. .-.. ---         .-- --- .-. .-.. -..')
        self.assertEqual(convert_text('ThIs Is A TeSt'),
                         '- .... .. ...         .. ...         .-         - . ... -')

    def test_invalid_character(self):
        with self.assertRaises(KeyError):
            convert_text('@')

    def test_empty_input(self):
        self.assertEqual(convert_text(''), '')
