import pytest
from typing import List

# We'll implement this function in the main code file
from top_k_frequent_words import top_k_frequent_words

def test_example_1():
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    expected = ["i", "love"]
    assert top_k_frequent_words(words, k) == expected

def test_tie_breaker():
    words = ["a", "b", "c", "a", "b", "c"]
    k = 2
    # All have same frequency, so alphabetical order
    assert top_k_frequent_words(words, k) == ["a", "b"]

def test_k_equals_unique():
    words = ["apple", "banana", "apple", "orange", "banana", "kiwi"]
    k = 4
    assert top_k_frequent_words(words, k) == ["apple", "banana", "kiwi", "orange"]

def test_single_word():
    words = ["unique"]
    k = 1
    assert top_k_frequent_words(words, k) == ["unique"] 