# six digit number
# value within range given in puzzle
import collections
import operator

class Solution():
    def __init__(self, password_range: str):
        self.lower_limit = int(password_range[:6])
        self.upper_limit = int(password_range[7:])
        self.password = [str(n) for n in range(self.lower_limit, self.upper_limit)]

    def one(self) -> int:
        # going from left to right, the digits never decrease
        self.password = [n for n in self.password if n == "".join(sorted(n))]    
        # two adjacent digits are the same
        self.password = [n for n in self.password if any(map(operator.eq, n, n[1:]))]
        return len(self.password)

    def two(self) -> int:
        return sum((1 for n in self.password if 2 in collections.Counter(n).values()))