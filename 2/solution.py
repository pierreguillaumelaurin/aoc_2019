from typing import Any, List, NoReturn

class Computer():
    def __init__(self, startup_computer_intcode: str) -> NoReturn:
        self.opcode = {1: sum, 2: self.prod, 99: 'exit'}
        self.intcode = [int(n) for n in startup_computer_intcode.split(',')]
        self.current_op_position = 0

    def first_solution(self) -> int:
        #self.fix()
        self.run()
        return self.intcode
            
    def run(self) -> NoReturn:
        current_operation = self.intcode[self.current_op_position]
        while self.execute(current_operation) != 'exit':
            first_input_position = self.current_op_position + 1
            second_input_position = self.current_op_position + 2
            output_position = self.current_op_position + 3
            input_cells = [self.intcode[self.intcode[first_input_position]], self.intcode[self.intcode[second_input_position]]]
            self.intcode[self.intcode[output_position]] = self.execute(current_operation)(input_cells)
            self.current_op_position += 4
            current_operation = self.intcode[self.current_op_position]

    def execute(self, op_position: int) -> Any:
        return self.opcode[op_position]

    def fix(self) -> NoReturn:
        self.intcode[1] = 12
        self.intcode[2] = 2
        
    @staticmethod
    def prod(it: List) -> int:
        res = 1
        for n in it:
            res *= n
        return res