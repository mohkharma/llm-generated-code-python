import threading

class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.lock = threading.Lock()
        self.cond = threading.Condition(self.lock)
        self.zero_turn = True
        self.even_turn = False
        self.odd_turn = False
        self.count = 0

    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        for _ in range(self.n * 2):
            with self.cond:
                while not self.zero_turn:
                    self.cond.wait()
                printNumber(0)
                self.count += 1
                if self.count % 2 == 0:
                    self.zero_turn = False
                    self.even_turn = True
                else:
                    self.zero_turn = False
                    self.odd_turn = True
                self.cond.notify_all()

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(2, self.n * 2 + 1, 2):
            with self.cond:
                while not self.even_turn:
                    self.cond.wait()
                printNumber(i)
                self.even_turn = False
                self.zero_turn = True
                self.cond.notify_all()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        for i in range(1, self.n * 2, 2):
            with self.cond:
                while not self.odd_turn:
                    self.cond.wait()
                printNumber(i)
                self.odd_turn = False
                self.zero_turn = True
                self.cond.notify_all()