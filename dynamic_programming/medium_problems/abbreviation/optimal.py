from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests
from dynamic_programming.medium_problems.abbreviation.test_resources.functionality_test_data import \
    functionality_test_data
from dynamic_programming.medium_problems.abbreviation.test_resources.time_complexity_test_data import \
    time_complexity_test_data
from tools.logging.recursion import log_recursion


def optimal_abbreviations(**kwargs) -> str:
    a: str = kwargs["a"]
    b: str = kwargs["b"]
    abbreviation: Abbreviation = Abbreviation(a, b)
    result: bool = abbreviation.a_can_become_an_abbreviation_of_b()
    print(f"final result: {result}")
    if result:
        return "YES"
    else:
        return "NO"


class Abbreviation:
    def __init__(self, a: str, b: str):
        self.a: str = a
        self.b: str = b
        self.recursion_level: int = 0

    def a_can_become_an_abbreviation_of_b(self) -> bool:
        return self.search_for_abbreviation(self.a, index=0)

    def search_for_abbreviation(self, a: str, index: int) -> bool:
        log_recursion(self.recursion_level, index=index, a=a, b=self.b)
        self.recursion_level += 1


if __name__ == '__main__':
    functionality_test_data.update(time_complexity_test_data)
    dynamically_generate_tests(functionality_test_data, optimal_abbreviations, timed=True, timeout=2)
    run_dynamic_tests()
