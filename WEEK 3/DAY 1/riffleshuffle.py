import unittest


def is_single_riffle(half1, half2, shuffled_deck):
    indi1 = 0
    indi2 = 0
    maxindi1 = len(half1) - 1
    maxindi2 = len(half2) - 1

    for card in shuffled_deck:
        if indi1 <= maxindi1 and card == half1[indi1]:
            indi1 += 1
        elif indi2 <=maxindi2 and card == half2[indi2]:
            indi2 += 1
        else:
            return False
    return True


















# Tests

class Test(unittest.TestCase):

    def test_both_halves_are_the_same_length(self):
        result = is_single_riffle([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_halves_are_different_lengths(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_half_is_empty(self):
        result = is_single_riffle([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_shuffled_deck_is_missing_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_shuffled_deck_has_extra_cards(self):
        result = is_single_riffle([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)


unittest.main(verbosity=2)