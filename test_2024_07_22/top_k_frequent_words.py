from typing import List

def top_k_frequent_words(words: List[str], k: int) -> List[str]:
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    return sorted(word_count.keys(), key=lambda x: (-word_count[x], x))[:k] 