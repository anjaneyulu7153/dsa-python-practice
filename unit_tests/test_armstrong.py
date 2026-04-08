import pytest
from src.math.armstrong_number.armstrong_number import ArmstrongRangeFinder


class TestArmstrong:

    def setup_method(self):
        """Initialize object before each test"""
        self.finder = ArmstrongRangeFinder()

    # -------------------------------
    # ✅ Test is_armstrong()
    # -------------------------------

    @pytest.mark.parametrize("num, expected", [
        (0, True),
        (1, True),
        (5, True),
        (9, True),
        (10, False),
        (153, True),
        (370, True),
        (371, True),
        (407, True),
        (100, False),
        (9474, True),
        (9475, False),
    ])
    def test_is_armstrong(self, num, expected):
        """Test Armstrong number validation"""
        assert self.finder.is_armstrong(num) == expected

    # -------------------------------
    # ✅ Test count_digits()
    # -------------------------------

    @pytest.mark.parametrize("num, expected", [
        (0, 1),
        (5, 1),
        (10, 2),
        (153, 3),
        (9999, 4),
    ])
    def test_count_digits(self, num, expected):
        """Test digit counting"""
        assert self.finder.count_digits(num) == expected

    # -------------------------------
    # ✅ Test find_in_range()
    # -------------------------------

    def test_find_in_range_basic(self):
        """Test range 1 to 1000"""
        result = self.finder.find_in_range(1, 1000)
        expected = [1,2,3,4,5,6,7,8,9,153,370,371,407]
        assert result == expected

    def test_find_in_range_single(self):
        """Test single number range"""
        result = self.finder.find_in_range(153, 153)
        assert result == [153]

    def test_find_in_range_no_result(self):
        """Test range with no Armstrong numbers"""
        result = self.finder.find_in_range(200, 300)
        assert result == []

    def test_find_in_range_large(self):
        """Test full range"""
        result = self.finder.find_in_range(1, 10000)
        expected = [1,2,3,4,5,6,7,8,9,153,370,371,407,1634,8208,9474]
        assert result == expected
