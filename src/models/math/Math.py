import time
import numpy as np


class Math:
    def speed_test(func):
        def wrapper(self, list):
            start = time.time()
            func(self, list)
            end = time.time()
            print(f"time delta = {end - start}")
        return wrapper

    def squares_eval1(self, list):
        start = time.time()
        squared_numbers = []
        for i in list:
            squared_numbers.append(i**2)
        result = sum(squared_numbers)
        end = time.time()
        print(f"time delta = {end - start}")

    @speed_test
    def squares_eval2(self, list):
        result = sum([x**2 for x in list])

    def squares_eval3(self, list):
        start = time.time()
        # var part
        result = sum(map(lambda x: x**2, list))
        end = time.time()
        print(f"time delta = {end - start}")

    def squares_eval4(self, list):
        list_np = np.array(list)
        start = time.time()
        # var part
        result = np.sum(list_np**2)
        end = time.time()
        print(f"time delta = {end - start}")
