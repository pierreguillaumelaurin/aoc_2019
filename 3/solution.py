from typing import List, NoReturn, Tuple

class Solution():
    def __init__(self, first_wire_moves, second_wire_moves):
        first_wire_moves = first_wire_moves.split(',')
        second_wire_moves = second_wire_moves.split(',')
        self.direction_map = {'R': self.move_right, 'D': self.move_down, 'L': self.move_left, 'U': self.move_up}
        self.central_port = (0,0)
        # get wire positions
        self.first_wire_positions = [self.central_port]
        self.second_wire_positions = [self.central_port]
        
        self.trace(self.first_wire_positions, first_wire_moves)
        self.trace(self.second_wire_positions, second_wire_moves)

    def trace(self, wire_positions: List, wire_moves: List) -> NoReturn: 
         for move in wire_moves:
            direction_symbol = move[0]
            move_in_relevant_direction_function = self.direction_map[direction_symbol]

            steps = int(move[1:])
            move_in_relevant_direction_function(wire_positions, steps)

    def move_up(self, wire_positions: List, steps: int) -> NoReturn:
        for _ in range(0, steps):
            current_wire_head = wire_positions[-1]
            new_wire_head = (current_wire_head[0], current_wire_head[1] + 1)
            wire_positions.append(new_wire_head)        

    def move_down(self, wire_positions: List, steps: int) -> NoReturn:
        for _ in range(0, steps):
            current_wire_head = wire_positions[-1]
            new_wire_head = (current_wire_head[0], current_wire_head[1] - 1)
            wire_positions.append(new_wire_head)        


    def move_right(self, wire_positions: List, steps: int) -> NoReturn:
        for _ in range(0, steps):
            current_wire_head = wire_positions[-1]
            new_wire_head = (current_wire_head[0] + 1, current_wire_head[1])
            wire_positions.append(new_wire_head)        

    def move_left(self, wire_positions: List, steps: int) -> NoReturn:
        for _ in range(0, steps):
            current_wire_head = wire_positions[-1]
            new_wire_head = (current_wire_head[0] - 1, current_wire_head[1])
            wire_positions.append(new_wire_head)        

    def one(self) -> int:
        common_positions = self.get_common_positions()
        return min((self.get_manhattan_distance_from_central_port(pos) for pos in common_positions))

    def two(self) -> int:
        common_positions = self.get_common_positions()
        return min((sum((self.first_wire_positions.index(pos), self.second_wire_positions.index(pos))) for pos in common_positions))    

    def get_common_positions(self) -> List:
        first_wire_positions_without_tail = self.first_wire_positions[1:]
        second_wire_positions_without_tail = self.second_wire_positions[1:]
        return list(set(first_wire_positions_without_tail).intersection(second_wire_positions_without_tail))   

    def get_manhattan_distance_from_central_port(self, wire_head: Tuple) -> int:
        horizontal_distance = abs(wire_head[0] - self.central_port[0])
        vertical_distance = abs(wire_head[1] - self.central_port[1])

        return horizontal_distance + vertical_distance

# get shortest distance