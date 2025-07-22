from longest_substring import length_of_longest_substring

def test_example_1():
    s = "abcabcbb"
    assert length_of_longest_substring(s) == 3

def test_example_2():
    s = "bbbbb"
    assert length_of_longest_substring(s) == 1

def test_example_3():
    s = "pwwkew"
    assert length_of_longest_substring(s) == 3

def test_empty():
    s = ""
    assert length_of_longest_substring(s) == 0

def test_all_unique():
    s = "abcdefg"
    assert length_of_longest_substring(s) == 7

def test_all_same():
    s = "aaaaaa"
    assert length_of_longest_substring(s) == 1

def test_with_spaces_and_symbols():
    s = "a b!c@d#e$f%"
    assert length_of_longest_substring(s) == 12

def test_long_repeat_at_end():
    s = "abcddefg"
    assert length_of_longest_substring(s) == 4 