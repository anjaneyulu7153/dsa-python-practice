class Subarray:
    """
    Utility class for array manipulation operations.
    """

    def move_zeros_to_end(self, arr):
        """
        Moves all zeros to the end (optimal approach).

        Uses a two-pointer technique to shift non-zero elements forward
        while maintaining their relative order.

        Args:
            arr (list[int]): List of integers.

        Returns:
            list[int]: Modified list with zeros moved to the end.

        Time Complexity:
            O(n)

        Space Complexity:
            O(1)
        """
        j = 0

        for i in range(len(arr)):
            if arr[i] != 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1

        return arr

    def move_zeros_to_end_bruteforce(self, arr):
        """
        Moves all zeros to the end (brute-force approach).

        Builds a new list of non-zero elements and appends zeros at the end.

        Args:
            arr (list[int]): List of integers.

        Returns:
            list[int]: New list with zeros moved to the end.

        Time Complexity:
            O(n)

        Space Complexity:
            O(n)
        """
        non_zeros = []
        zero_count = 0

        for num in arr:
            if num != 0:
                non_zeros.append(num)
            else:
                zero_count += 1

        return non_zeros + [0] * zero_count

    def move_zeros_to_end_quadratic(self, arr):
        """
        Moves all zeros to the end (naive O(n^2) approach).

        For each zero found, shift it step-by-step toward the end
        by swapping with the next element repeatedly.

        Args:
            arr (list[int]): List of integers.

        Returns:
            list[int]: Modified list with zeros moved to the end.

        Time Complexity:
            O(n^2) - Nested shifting for each zero.

        Space Complexity:
            O(1) - In-place operation.
        """
        n = len(arr)

        for i in range(n):
            if arr[i] == 0:
                # Shift this zero to the right step by step
                for j in range(i, n - 1):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr


if __name__ == "__main__":
    subarray = Subarray()

    data = [1, 2, 0, 0, 4, 3, 6, 5, 0]

    print("Optimal:", subarray.move_zeros_to_end(data.copy()))
    print("Brute Force:", subarray.move_zeros_to_end_bruteforce(data.copy()))
    print("Quadratic:", subarray.move_zeros_to_end_quadratic(data.copy()))
