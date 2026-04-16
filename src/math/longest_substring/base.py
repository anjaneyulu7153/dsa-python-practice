class LongestSubstringSolutions:
    """
    Collection of approaches to solve
    'Longest Substring Without Repeating Characters'
    """

    def brute_force_n3(self, s: str) -> int:
        """
        O(n^3) approach:
        Generate all substrings and check uniqueness
        """
        def is_unique(sub):
            return len(set(sub)) == len(sub)

        n = len(s)
        max_length = 0

        for i in range(n):
            for j in range(i, n):
                substring = s[i:j+1]
                if is_unique(substring):
                    max_length = max(max_length, len(substring))

        return max_length

    def brute_force_n2(self, s: str) -> int:
        """
        O(n^2) approach:
        Expand substring dynamically using set
        """
        n = len(s)
        max_length = 0

        for i in range(n):
            seen = set()

            for j in range(i, n):
                if s[j] in seen:
                    break

                seen.add(s[j])
                max_length = max(max_length, j - i + 1)

        return max_length

    def sliding_window_set(self, s: str) -> int:
        """
        O(n) approach using SET
        Shrinks window step-by-step
        """
        char_set = set()
        left = 0
        max_length = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length

    def sliding_window_map(self, s: str) -> int:
        """
        O(n) optimized approach using HASHMAP
        Jumps left pointer directly
        """
        char_map = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in char_map:
                left = max(left, char_map[s[right]] + 1)

            char_map[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length


# ✅ Example usage
if __name__ == "__main__":
    obj = LongestSubstringSolutions()

    test_cases = [
        "abcabcbb",
        "bbbbb",
        "pwwkew",
        "abba",
        "abcdcjd"
    ]

    for s in test_cases:
        print(f"\nInput: {s}")
        print("O(n^3):", obj.brute_force_n3(s))
        print("O(n^2):", obj.brute_force_n2(s))
        print("Set O(n):", obj.sliding_window_set(s))
        print("Map O(n):", obj.sliding_window_map(s))
