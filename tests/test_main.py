from src.finder import Finder


class TestFinder:
    finder = Finder("*/15 0 1,15 * 1-5")

    def test_finder(self):
        
        self.finder.find_info()
        assert self.finder.dict_result == {
            "minute": [0, 15, 30, 45],
            "hour": [0],
            "day of month": [1, 15],
            "month": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
            "day of week": [1, 2, 3, 4, 5],
        }


    def test_check_symbol(self):
        assert self.finder._check_symbol("*/15", "minute") == None


    def test_validate_left_right(self):
        assert self.finder._validate_left_right([2, 3, 4, 5], 1, "minute") == None

    def test_count_left_right(self):
        assert self.finder._count_left_right([2, 3, 4, 5], 1) == [2, 3, 4, 5]


    def test_validate_left_right(self):
        assert self.finder._validate_left_right([2, 3, 4, 5], 1, "minute") == None

    def test__count_left_right(self):
        assert self.finder._count_left_right([2, 3, 4, 5], 1) == [2, 3, 4, 5]
    
    def test_separate_expression(self):
        assert self.finder._separate_expression("*/15", "minute") == [0, 15, 30, 45]