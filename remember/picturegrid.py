grid = [[".", ".", ".", ".", ".", "."],
        [".", "0", "0", ".", ".", "."],
        ["0", "0", "0", "0", ".", "."],
        ["0", "0", "0", "0", "0", "."],
        [".", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "."],
        ["0", "0", "0", "0", ".", "."],
        [".", "0", "0", ".", ".", "."],
        [".", ".", ".", ".", ".", "."]]


y = len(grid) #9
x = len(grid[0]) #6
start = 0

for y1 in range(x):
    print()
    for start in range(y):
        print(grid[start][y1], end="")
        start += 1