# from output.claude.Task18_CLAUDE_claude_3_5_sonnet_20240620 import binary_array_to_number as convert_binary_array_to_int
# from output.codestral.Task18_MISTRAL_codestral_latest import binary_array_to_number as convert_binary_array_to_int
# from output.gemini.Task18_GEMINI_gemini_1_5_pro_001 import binary_array_to_number as convert_binary_array_to_int
# from output.gtp4o.Task18_OPENAI_gpt_4o import binary_array_to_int as convert_binary_array_to_int
# from output.llama3.Task18_PERPLEXITY_llama_3_sonar_large_32k_chat import binary_array_to_number as convert_binary_array_to_int
import unittest

class TestBinaryConversion(unittest.TestCase):

    def test_basic_example1(self):
        # Test with basic example where the array represents binary 1
        self.assertEqual(convert_binary_array_to_int([0, 0, 0, 1]), 1)

    def test_basic_example2(self):
        # Test with basic example where the array represents binary 2
        self.assertEqual(convert_binary_array_to_int([0, 0, 1, 0]), 2)

    def test_basic_example3(self):
        # Test with basic example where the array represents binary 5
        self.assertEqual(convert_binary_array_to_int([0, 1, 0, 1]), 5)

    def test_duplicate_value(self):
        # Test with an array where the binary value is 2
        self.assertEqual(convert_binary_array_to_int([0, 0, 1, 0]), 2)

    def test_binary6(self):
        # Test with an array where the binary value is 6
        self.assertEqual(convert_binary_array_to_int([0, 1, 1, 0]), 6)

    def test_binary15(self):
        # Test with an array where the binary value is 15
        self.assertEqual(convert_binary_array_to_int([1, 1, 1, 1]), 15)

    def test_binary11(self):
        # Test with an array where the binary value is 11
        self.assertEqual(convert_binary_array_to_int([1, 0, 1, 1]), 11)

    def test_single_bit1(self):
        # Test with an array representing a single bit of 1
        self.assertEqual(convert_binary_array_to_int([1]), 1)

    def test_single_bit0(self):
        # Test with an array representing a single bit of 0
        self.assertEqual(convert_binary_array_to_int([0]), 0)

    def test_longer_array(self):
        # Test with a longer array representing binary 43
        self.assertEqual(convert_binary_array_to_int([0, 1, 0, 1, 0, 1, 1]), 43)

if __name__ == "__main__":
    unittest.main()