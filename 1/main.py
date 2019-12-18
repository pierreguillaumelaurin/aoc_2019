from solution import Solution

if __name__ == "__main__":
    lines = []
    while True:
        line = input()
        if line:
             lines.append(line)
        else:
             break

    solution = Solution(lines)
    print(solution.one())
    print(solution.two())