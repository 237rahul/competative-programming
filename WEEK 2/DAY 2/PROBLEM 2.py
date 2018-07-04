import unittest


def is_valid(code):
    dict1 = {
        '(' : ')',
        '{' : '}',
        '[' : ']',
    }
    opens = set(dict1.keys())
    closes = set(dict1.values())
    stack = []
    for entry in code:
        if entry in opens:
            stack.append(entry)
        elif entry in closes:
            if not stack:
                return False
            else:
                last_unclosed_opener = stack.pop()
                if not dict1[last_unclosed_opener] == entry:
                    return False

    return stack == []


















# Tests

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)


unittest.main(verbosity=2)