from solution import Solution

if __name__ == "__main__":
    lines = []
    while True:
        line = input()
        if line:
             lines.append(line)
        else:
             break

    solution = Solution()
    print(solution.one(lines))
    print(solution.two(lines))