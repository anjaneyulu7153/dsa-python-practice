class SortColors:
    """
    Provides methods to sort arrays with:
    1. Exactly 3 distinct values (Dutch National Flag)
    2. General values using counting sort
    """

    def sort_three_values(self, arr, a, b, c):
        """
        Sort array containing exactly 3 distinct values: a, b, c

        Example:
        arr = [3,4,5,3,4,5], a=3, b=4, c=5

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        low = 0
        mid = 0
        high = len(arr) - 1

        while mid <= high:
            if arr[mid] == a:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1

            elif arr[mid] == b:
                mid += 1

            else:  # arr[mid] == c
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1

        return arr

    def counting_sort(self, arr):
        """
        General approach for non-negative integers

        Time Complexity: O(n + k)
        Space Complexity: O(k)
        where k = max(arr)
        """
        if not arr:
            return arr

        max_val = max(arr)
        count = [0] * (max_val + 1)

        # Count frequency
        for num in arr:
            count[num] += 1

        # Rebuild array
        i = 0
        for num in range(len(count)):
            while count[num] > 0:
                arr[i] = num
                i += 1
                count[num] -= 1

        return arr

sc = SortColors()

# Optimized 3-value case
print(sc.sort_three_values([3,4,5,3,4,5], 3, 4, 5))

# General case
print(sc.counting_sort([3,4,5,3,4,5]))
