import datetime as dt


class Timer:
    def __init__(self) -> None:
        pass

    def what_time() -> str:
        now = dt.datetime.now()
        return now.strftime('%Y-%m-%d %H:%M:%S')
