from typing import Set

def length_of_longest_substring(s: str) -> int:
    n = len(s)
    if n == 0:
        return 0
    seen: Set[str] = set()
    left = 0
    max_len = 0
    for right in range(n):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)
    return max_len 