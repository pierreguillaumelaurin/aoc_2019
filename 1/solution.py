from typing import List, NoReturn

class Solution():
    def __init__(self, usr_input: List[int]) -> NoReturn:
       self.converted_usr_input = self.str_to_int(usr_input)
    
    def one(self) -> int:
       return sum([self.get_fuel_requirements(n) for n in self.converted_usr_input])

    def two(self) -> int:
       return sum([self.get_total_fuel_requirements(n) for n in self.converted_usr_input])
       
    def get_total_fuel_requirements(self, added_object: int) -> int:
       fuel_requirements = self.get_fuel_requirements(added_object)
       if fuel_requirements <= 0:
          return 0
       else:
         return fuel_requirements + self.get_total_fuel_requirements(fuel_requirements) 

    @staticmethod
    def get_fuel_requirements(added_object: int) -> int:
       return int(float(added_object)/3) - 2

    @staticmethod
    def str_to_int(usr_input: List[str]) -> List[int]:
       return [int(n) for n in usr_input]
