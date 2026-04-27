class ContainerWithMostWater:
    """
    Solve 'Container With Most Water' problem using:
    1. Brute Force
    2. Optimized Two-Pointer Approach
    """

    def brute_force(self, arr):
        """
        Check all pairs

        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(arr)
        max_area = 0

        for i in range(n - 1):
            for j in range(i + 1, n):
                area = min(arr[i], arr[j]) * (j - i)
                max_area = max(max_area, area)

        return max_area

    def two_pointer(self, arr):
        """
        Optimized approach using two pointers

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        left = 0
        right = len(arr) - 1
        max_area = 0

        while left < right:
            area = min(arr[left], arr[right]) * (right - left)
            max_area = max(max_area, area)

            # Move the smaller height
            if arr[left] < arr[right]:
                left += 1
            else:
                right -= 1

        return max_area
obj = ContainerWithMostWater()

arr = [3, 1, 2, 4, 5]

# Brute Force
print("Brute Force:", obj.brute_force(arr))

# Optimized
print("Two Pointer:", obj.two_pointer(arr))
