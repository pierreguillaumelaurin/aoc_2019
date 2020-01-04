# six digit number
# value within range given in puzzle
import collections
import operator

class Solution():
    def __init__(self, password_range: str):
        self.lower_limit = int(password_range[:6])
        self.upper_limit = int(password_range[7:])
        self.passwords = [str(n) for n in range(self.lower_limit, self.upper_limit)]

    def one(self) -> int:
        # going from left to right, the digits never decrease
        self.passwords = [n for n in self.passwords if n == "".join(sorted(n))]    
        # two adjacent digits are the same
        self.passwords = [n for n in self.passwords if any(map(operator.eq, n, n[1:]))]
        return len(self.passwords)

    def two(self) -> int:
        return sum((1 for n in self.passwords if 2 in collections.Counter(n).values()))