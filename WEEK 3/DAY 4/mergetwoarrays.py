import unittest


def merge_lists(my_list, alices_list):
    list_size = len(my_list) + len(alices_list)
    lis1 = [None] * list_size

    alices = 0
    mine = 0
    merged = 0
    while merged < list_size:
        is_my_list_exhausted = mine >= len(my_list)
        is_alices_list_exhausted = alices >= len(alices_list)
        if (not is_my_list_exhausted and
                (is_alices_list_exhausted or
                 my_list[mine] < alices_list[alices])):
            lis1[merged] = my_list[mine]
            mine += 1
        else:
            lis1[merged] = alices_list[alices]
            alices += 1

        merged += 1

    return lis1


















# Tests

class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)