class Jar:
    def __init__(self, capacity=12):
        if capacity < 0:
            raise ValueError("Capacity can't be negative")
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if not isinstance(n, int):
            raise ValueError("Please input integer while depositing")
        if n < 0:
            raise ValueError("Can not deposit negative amount Cookies")
        if self._size + n > self._capacity:
            raise ValueError("Jar Capacity Exceeded")
        self._size = self._size + n

    def withdraw(self, n):
        if not isinstance(n, int):
            raise ValueError("Please input integer while withdrowing")
        if n < 0:
            raise ValueError("Withdraw amount must be positive")
        if self._size - n < 0:
            raise ValueError("You ate all the cookies!")
        self._size = self._size - n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
