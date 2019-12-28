import computer
from typing import Tuple

class Solution():
    def __init__(self, usr_input):
        self.elve_computer = computer.Computer(usr_input)

    def first_solution(self) -> int:
        return self.elve_computer.set_run_and_reset(12, 2)

    def second_solution(self) -> int:
        for n in range(0, 100):
            for m in range(0, 100):
                if self.elve_computer.set_run_and_reset(n, m) == 2:
                    return 100 * n + m