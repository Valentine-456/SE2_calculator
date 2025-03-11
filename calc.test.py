import unittest

from calc import strToNumSum


class TestCalculations(unittest.TestCase):

    def test_empty_string_param_should_return_0(self):
        input = ""

        result = strToNumSum(input)

        self.assertEqual(result, 0)

    def test_simple_number_param_should_return_this_number(self):
        expectedOutput = 10
        input = str(expectedOutput)

        result = strToNumSum(input)

        self.assertEqual(result, expectedOutput)

    def test_2_numbers_coma_delimiter_should_return_sum(self):
        input = "1,2"
        expectedOutput = sum(map(int, input.split(",")))

        result = strToNumSum(input)

        self.assertEqual(result, expectedOutput)

    def test_2_numbers_newline_delimiter_should_return_sum(self):
        input = "1\n2"
        expectedOutput = sum(map(int, input.split("\n")))

        result = strToNumSum(input)

        self.assertEqual(result, expectedOutput)

    def test_numbers_separated_by_mixed_delimiters_should_return_sum(self):
        input = "5,6\n7"
        expectedOutput = 5 + 6 + 7

        result = strToNumSum(input)

        self.assertEqual(result, expectedOutput)

    def test_have_negative_number_should_raise_exception(self):
        input = "5,-6\n7"
        
        with self.assertRaises(ArithmeticError):
            strToNumSum(input)

    def test_big_numbers_included_should_be_ignored_in_sum(self):
        numbers = [1, 2, 3, 1400, 50000]
        expectedOutput = sum(filter(lambda x: x <= 1000, numbers))
        input = ",".join(map(str, numbers))

        result = strToNumSum(input)

        self.assertEqual(expectedOutput, result)

    def test_custom_delimiter_on_first_line(self):
        param = "//#\n1#2#3"
        expectedOutput = 1 + 2 + 3

        result = strToNumSum(param)

        self.assertEqual(result, expectedOutput)

    def test_multichar_custom_delimiter_on_first_line(self):
        param = "//[###]\n1###2,3"
        expectedOutput = 1 + 2 + 3

        result = strToNumSum(param)

        self.assertEqual(result, expectedOutput)

    def test_multiple_custom_delimiters_should_work(self):
        input = "//[###][joker][&]\n1###2joker3&4"
        expectedOutput = 1 + 2 + 3 + 4

        result = strToNumSum(input)

        self.assertEqual(result, expectedOutput)


unittest.main()
