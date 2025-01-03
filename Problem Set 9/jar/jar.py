class Jar:
    def __init__(self, capacity=12):
        self._size = 0
        if capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError("Invalid capacity")

    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        if n + self._size <= self.capacity:
            self._size += n
        else:
            raise ValueError("Invalid number of cookies")

    def withdraw(self, n):
        if n <= self._size:
            self._size -= n
        else:
            raise ValueError("Invalid number of cookies")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size
