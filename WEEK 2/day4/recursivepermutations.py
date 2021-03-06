import unittest


def get_permutations(string):

    # Generate all permutations of the input string
    if len(string)<=1:
        return set([string])
    lastbutone=string[:-1]
    last=string[-1]
    permutations=get_permutations(last)
    permutations1=set()
    for i in permutations:
        for j in range(len(last)+1):
            permutation=i[:j]+last+i[j:]
            permutations1.add(per)
    return permutations1


















# Tests

class Test(unittest.TestCase):

    def test_empty_string(self):
        actual = get_permutations('')
        expected = set([''])
        self.assertEqual(actual, expected)

    def test_one_character_string(self):
        actual = get_permutations('a')
        expected = set(['a'])
        self.assertEqual(actual, expected)

    def test_two_character_string(self):
        actual = get_permutations('ab')
        expected = set(['ab', 'ba'])
        self.assertEqual(actual, expected)

    def test_three_character_string(self):
        actual = get_permutations('abc')
        expected = set(['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)