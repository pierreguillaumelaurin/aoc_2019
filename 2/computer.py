from typing import Any, List, NoReturn

class Computer():
    def __init__(self, startup_computer_intcode: str) -> NoReturn:
        self.opcode = {1: sum, 2: self.prod, 99: 'exit'}
        self.intcode = [int(n) for n in startup_computer_intcode.split(',')] 
        self.current_op_position = 0
        self.program_alarm_state = self.get_program_alarm_state()
        self.reset_memory()

    def get_program_alarm_state(self) -> List:
        self.intcode[1] = 12
        self.intcode[2] = 2 
        self.run()
        return self.intcode


    def set_run_and_reset(self, noun: int, verb: int) -> int:
        self.set_inputs(noun, verb)
        output = self.run()
        self.reset_memory()
        return output


    def run(self) -> int:
        current_operation = self.intcode[self.current_op_position]
        while self.execute(current_operation) != 'exit':
            first_input_position = self.intcode_to_position(self.current_op_position + 1)
            second_input_position = self.intcode_to_position(self.current_op_position + 2)
            output_position = self.intcode_to_position(self.current_op_position + 3)
            input_cells = [self.intcode[first_input_position], self.intcode[second_input_position]]

            self.intcode[output_position] = self.execute(current_operation)(input_cells)
            self.current_op_position += 4
            current_operation = self.intcode[self.current_op_position]
        return self.intcode[0]    

    def intcode_to_position(self, intcode_cell: int) -> int:
        return self.intcode[intcode_cell]

    def execute(self, op_position: int) -> Any:
        return self.opcode[op_position]

    def set_inputs(self, noun: int, verb: int) -> NoReturn:
        self.intcode[1] = noun
        self.intcode[2] = verb 

    def reset_memory(self) -> NoReturn:
        self.intcode = self.program_alarm_state

    @staticmethod
    def prod(it: List) -> int:
        res = 1
        for n in it:
            res *= n
        return res