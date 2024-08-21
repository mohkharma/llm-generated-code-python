# from output.claude.Task21_CLAUDE_claude_3_5_sonnet_20240620 import remove_smallest as remove_smallest
# from output.codestral.Task21_MISTRAL_codestral_latest import remove_smallest as remove_smallest
# from output.gemini.Task21_GEMINI_gemini_1_5_pro_001 import remove_smallest as remove_smallest
# from output.gtp4o.Task21_OPENAI_gpt_4o import remove_smallest as remove_smallest
# from output.llama3.Task21_PERPLEXITY_llama_3_sonar_large_32k_chat import remove_smallest as remove_smallest
import unittest


class TestRemoveSmallest(unittest.TestCase):

    def test_case1(self):
        input_data = [1, 2, 3, 4, 5]
        expected = [2, 3, 4, 5]
        self.assertEqual(remove_smallest(input_data), expected)

    def test_case2(self):
        input_data = [5, 3, 2, 1, 4]
        expected = [5, 3, 2, 4]
        self.assertEqual(remove_smallest(input_data), expected)

    def test_case3(self):
        input_data = [2, 2, 1, 2, 1]
        expected = [2, 2, 2, 1]
        self.assertEqual(remove_smallest(input_data), expected)

    def test_case4(self):
        input_data = [1]
        expected = []
        self.assertEqual(remove_smallest(input_data), expected)

    def test_case5(self):
        input_data = [1, 1, 1, 1]
        expected = [1, 1, 1]
        self.assertEqual(remove_smallest(input_data), expected)

    def test_case6(self):
        input_data = []
        expected = []
        self.assertEqual(remove_smallest(input_data), expected)

    def test_case7(self):
        input_data = [2, 3, 2, 3, 1]
        expected = [2, 3, 2, 3]
        self.assertEqual(remove_smallest(input_data), expected)

    def test_case8(self):
        input_data = [7, 7, 7, 7, 7]
        expected = [7, 7, 7, 7]
        self.assertEqual(remove_smallest(input_data), expected)

    def test_case9(self):
        input_data = [5, 6, 7, 8, 9]
        expected = [6, 7, 8, 9]
        self.assertEqual(remove_smallest(input_data), expected)

    def test_case10(self):
        input_data = [10, 10, 10]
        expected = [10, 10]
        self.assertEqual(remove_smallest(input_data), expected)

if __name__ == '__main__':
    unittest.main()