from typing import Callable, List


ConditionFunction = Callable[[int], bool]


class Filter:
    @classmethod
    def filter_list(cls, list: List[int], condition: ConditionFunction) -> List[int]:
        return [i for i in list if condition(i)]
