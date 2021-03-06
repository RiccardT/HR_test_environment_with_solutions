from test_utilities.dynamic_test_creator import \
    dynamically_generate_tests, run_dynamic_tests
from searching.medium_problems.ice_cream_parlor.test_resources.functionality_test_data import functionality_test_data


def brute_force(trips: list) -> list:
    flavor_pairs: list = []
    for trip in trips:
        money: int = trip["money"]
        cost: list = trip["cost"]
        distinct_ice_cream_flavors: list = get_optimal_ice_cream_purchases(money, cost)
        flavor_pairs.append(distinct_ice_cream_flavors)
    return flavor_pairs


def get_optimal_ice_cream_purchases(money: int, cost: list) -> list:  # O(n^2)
    distinct_flavors: list = []
    for i, ice_cream_1 in enumerate(cost):
        for j, ice_cream_2 in enumerate(cost):
            if i == j:
                continue
            else:
                if ice_cream_1 + ice_cream_2 == money:
                    distinct_flavors.append(i + 1)
                    distinct_flavors.append(j + 1)
                    break
        if len(distinct_flavors) == 2:
            break
    sorted_distinct_flavors: list = sorted(distinct_flavors)
    return sorted_distinct_flavors


if __name__ == '__main__':
    dynamically_generate_tests(functionality_test_data, brute_force)
    run_dynamic_tests()

