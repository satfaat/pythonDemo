import time
import random


class DemoList:
    def create_list(self, LIMIT):
        list = [random.random() for _ in range(LIMIT)]
        return list
