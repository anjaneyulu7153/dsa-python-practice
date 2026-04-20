class TimeComplexityDemo:
    """
    A class to demonstrate different time complexities using simple operations
    on a list of integers.
    """

    def __init__(self):
        """
        Initialize with a list of 10 different integers.
        Time Complexity: O(1)
        """
        self.nums = [3, 7, 2, 9, 1, 5, 8, 6, 4, 10]

    def constant_time(self):
        """
        Access the first element of the list.

        Explanation:
        No matter the size of the list, accessing an element by index
        always takes the same time.

        Time Complexity: O(1)
        """
        return self.nums[0]

    def linear_time(self):
        """
        Iterate through the list and print each element.

        Explanation:
        The loop runs once for each element.

        Time Complexity: O(n)
        """
        for num in self.nums:
            print(num)

    def linear_search(self, target):
        """
        Search for a target element in the list.

        Explanation:
        In the worst case, we check all elements.

        Time Complexity:
        - Best Case: O(1)
        - Worst Case: O(n)
        """
        for num in self.nums:
            if num == target:
                return True
        return False

    def quadratic_time(self):
        """
        Print all pairs of elements.

        Explanation:
        Nested loops → each element compares with every other.

        Time Complexity: O(n^2)
        """
        for i in self.nums:
            for j in self.nums:
                print(i, j)

    def cubic_time(self):
        """
        Triple nested loop demonstration.

        Explanation:
        Used to show how quickly complexity increases.

        Time Complexity: O(n^3)
        """
        for i in self.nums:
            for j in self.nums:
                for k in self.nums:
                    pass  # Just iterating

    def logarithmic_time(self, target):
        """
        Perform binary search (requires sorted list).

        Explanation:
        Each step halves the search space.

        Time Complexity: O(log n)
        """
        nums_sorted = sorted(self.nums)
        left, right = 0, len(nums_sorted) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums_sorted[mid] == target:
                return True
            elif nums_sorted[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def n_log_n_time(self):
        """
        Sort the list.

        Explanation:
        Python's built-in sort uses Timsort.

        Time Complexity: O(n log n)
        """
        return sorted(self.nums)

    def exponential_time(self, n):
        """
        Recursive Fibonacci (inefficient version).

        Explanation:
        Each call branches into two → exponential growth.

        Time Complexity: O(2^n)
        """
        if n <= 1:
            return n
        return self.exponential_time(n - 1) + self.exponential_time(n - 2)

    def factorial_time(self, n):
        """
        Generate all permutations (conceptual example).

        Explanation:
        Number of permutations grows factorially.

        Time Complexity: O(n!)
        """
        if n == 0:
            return 1
        return n * self.factorial_time(n - 1)

    def space_example(self):
        """
        Create a new list.

        Explanation:
        Additional space grows with input size.

        Space Complexity: O(n)
        """
        new_list = [x * 2 for x in self.nums]
        return new_list
