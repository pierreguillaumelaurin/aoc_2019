from typing import Any, NoReturn

class Computer():
    def __init__(self, startup_computer_intcode: str) -> NoReturn:
        self.opcode = {1: sum, 2: self.prod, 99: 'exit'}
        self.intcode = [int(n) for n in startup_computer_intcode.split(',')]
        self.current_op_position = 0

    def first_solution(self) -> int:
        self.fix()
        self.run()
        return getattr(self, self.intcode)[0]
            
    def run(self) -> NoReturn:
        current_operation = self.intcode[self.current_op_position]
        while self.execute(current_operation) != 'exit':
            first_input_position = self.current_op_position + 1
            second_input_position = self.current_op_position + 2
            output_position = self.current_op_position + 3
            self.intcode[output_position] = self.execute(current_operation)(self.intcode[first_input_position], self.intcode[second_input_position])
            self.current_op_position += 4
    
    def execute(self, op_position: int) -> Any:
        return self.opcode[op_position]

    def fix(self) -> NoReturn:
        self.intcode[1] = 12
        self.intcode[2] = 2
        
    @staticmethod
    def prod(first: int, second: int) -> int:
        return first * second