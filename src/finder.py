import string


class Finder:
    dates = {
        "minute": list(range(60)),
        "hour": list(range(24)),
        "day of month": list(range(1, 32)),
        "month": list(range(1, 13)),
        "day of week": list(range(1, 8)),
    }
    spec_symbols = ["/", "*", ",", "-"]

    def __init__(self, cron: str, command = "Library import"):
        self.cron = cron.strip()
        self.command = command
        self.cron_list = []
        self.dict_result = {}

    def __str__(self) -> str:
        """
        Optimisation:
        for make print process faster, we can name the print_result and compare whether it already exists and return the ready result
        """
        result = []
        for i in self.dict_result:
            result.append(f"{i:<20}{self.__list_int_to_str(self.dict_result[i])}\n")
        result.append(f"{'command':<20}{self.command}")
        return "".join(result)

    def __list_int_to_str(self, data: list[int]) -> str:
        """
        Return a string list instead of int list
        """
        return " ".join([str(x) for x in data])

    def _check_cron_expression(self):
        """
        Check if we have a valid cron expression.
        Should be equal 5 (minute, hour, day of month, month, day of week)
        """
        self.cron_list = self.cron.split(" ")
        if len(self.cron_list) != 5:
            raise ValueError("Invalid cron expression")

    def _merge_date(self) -> dict[str, list[int]]:
        """
        Merge the date and return a dictionary of the result
        """
        result = {}
        for zi, i in enumerate(self.dates):
            dates_list = self._calculate_date(self.cron_list[zi], i)
            result[i] = dates_list
        return result

    def _calculate_date(self, symbol: str, date: str) -> list[int]:
        """
        Calculate the date and return a list of the result
        """
        self._check_symbol(symbol, date)
        dates_list = self._separate_expression(symbol, date)
        return dates_list

    def _find_period(self, separated_symbol: str) -> list[str, int]:
        """
        Find left and reight expression and return the result
        If "/" not exists we can count the right side as 1, because the right meaning is the step number that equals 1
        """
        period_expression = separated_symbol.split("/")
        if len(period_expression) > 2:
            raise ValueError("Invalid period the / symbol should be only one")
        elif len(period_expression) == 1:
            return period_expression[0], 1
        try:
            return period_expression[0], int(period_expression[1])
        except ValueError:
            raise ValueError(
                f"the invalid value after /\nExpected int but got '{period_expression[1]}'"
            )

    def _parse_left_date(self, left: str, date: str) -> list[int]:
        """
        Parse the left expression and return the result
        In the main meaning there should be either '*' or expression that includes '-'
        Attention!!! we can accept the int (Example: 4) only if the right expression equals 1
        Good result: 1-10  or *
        """
        if left == "*":
            return self.dates[date]
        elif "-" in left:
            lift_sep = left.split("-")
            return list(range(int(lift_sep[0]), int(lift_sep[1]) + 1))
        try:
            return [int(left)]
        except ValueError:
            raise ValueError(f"Invalid expression in {date}.\nExpected int value but got '{left}'")

    def _separate_expression(self, symbol: str, date: str) -> list[int]:
        """
        Separate the expression and return the result
        The main separation should be with "," 
        The seccond separation should be with "/"
        The last separation should be with "-"
        """
        data = []
        for i in symbol.split(","):
            left_str, right_int = self._find_period(i)
            left_list = self._parse_left_date(left_str, date)
            self._validate_left_right(left_list, right_int, date)
            count_result = self._count_left_right(left_list, right_int)
            data.append(count_result)
        return sorted(list(set([element for sublist in data for element in sublist])))

    def _count_left_right(self, left: list[int], right: int) -> list[int]:
        return [x for x in range(left[0], left[-1] + 1, right)]

    def _validate_left_right(self, left: list[int], right: int, date: str) -> None:
        """
        Check if the left and right symbols are valid 
        Good result: 2-10/5
        Bad result: 2-10/ 
        """
        if len(left) == 1 and right != 1:
            raise ValueError(f"Invalid {date} expression")
        elif left[-1] > self.dates[date][-1]:
            raise ValueError(
                f"Invalid {date} expression\nExpected max value {self.dates[date][-1]} but got {left[-1]}"
            )

    def _check_symbol(self, symbol: str, date: str) -> None:
        """
        Check if the symbol is valid
        """
        if symbol == "":
            raise ValueError(f"Invalid {date}")
        if not all(
            [
                True if (x in string.digits or x in self.spec_symbols) else False
                for x in symbol
            ]
        ):
            raise ValueError(f"Invalid Spec symbol")

    def find_info(self):
        """
        Find the result of the cron expression
        """
        self._check_cron_expression()
        self.dict_result = self._merge_date()