from solution import Solution

if __name__ == "__main__":
    with open('input.txt', 'r') as file:
        lines = file.readlines()

    solution = Solution(lines[0], lines[1])
    print(solution.one())