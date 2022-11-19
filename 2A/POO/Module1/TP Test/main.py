from threading import Thread
import time


def function():
    global a
    time.sleep(0.5)
    a = 1 + 2


def func(var):
    vart = var


class Test:
    def __init__(self) -> None:
        self.var = "test"

    def test(self, var):
        self.var = var


if __name__ == "__main__":
    a = 0

    th2: Thread = Thread(target=function, name="pas sympa")
    th2.start()
    print(a)
    time.sleep(1)
    print(a)
