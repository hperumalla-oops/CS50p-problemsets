class Jar:
    def __init__(self, capacity=12):
           if capacity<0:
                raise ValueError("invalid capacity")
           else:
                self._capacity = capacity
                self.number=0


    def __str__(self):
        return "🍪" * self.number

    def deposit(self, n):
      self.number=self.number+n
      if self.number>self._capacity:
        raise ValueError("Too many cookies for the jar")
      #else:
        # self.number=self.number+n


    def withdraw(self, n):
      self.number=self.number-n
      if self.number<0:
        raise ValueError("Too few cookies in the jar")
      #else:
        # self.number=self.number-n


    @property
    def capacity(self):
      return self._capacity


    @property
    def size(self):
      return self._number



