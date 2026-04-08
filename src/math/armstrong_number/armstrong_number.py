class ArmstrongRangeFinder:
    """
    Class to find Armstrong numbers within a given range
    using mathematical operations (% and //).
    """

    def count_digits(self, number: int) -> int:
        """
        Count the number of digits in a given number.

        Args:
            number (int): Input number

        Returns:
            int: Number of digits
        """
        if number == 0:
            return 1

        count = 0
        while number > 0:
            number //= 10
            count += 1
        return count

    def is_armstrong(self, number: int) -> bool:
        """
        Check whether a number is an Armstrong number.

        Args:
            number (int): Input number

        Returns:
            bool: True if Armstrong, False otherwise
        """
        digits = self.count_digits(number)

        temp = number
        total = 0

        while temp > 0:
            digit = temp % 10
            total += digit ** digits
            temp //= 10

        return total == number

    def find_in_range(self, start: int, end: int) -> list:
        """
        Find all Armstrong numbers in a given range.

        Args:
            start (int): Start of range
            end (int): End of range

        Returns:
            list: List of Armstrong numbers
        """
        result = []

        for num in range(start, end + 1):
            if self.is_armstrong(num):
                result.append(num)

        return result


# 🔍 Usage
if __name__ == "__main__":
    finder = ArmstrongRangeFinder()
    print(finder.find_in_range(1, 10000))
