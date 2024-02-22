# create the grid
grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# print the grid
def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) if num != 0 else "." for num in row))

print_grid(grid)


# check the move
def is_valid_move(grid, row, col, num):
    # check the line
    if num in grid[row]:
        return False

    # check the column
    if num in [grid[i][col] for i in range(9)]:
        return False

    # check 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if grid[i][j] == num:
                return False

    return True

# check if win
def is_game_over(grid):
    for row in grid:
        if 0 in row:
            return False
    return True

# user
def main():
    # print grid
    print("Grille initiale:")
    print_grid(grid)

    while not is_game_over(grid):
        # input user
        row = int(input("Number of the line (1-9) : ")) - 1
        col = int(input("Number of the column (1-9) : ")) - 1
        num = int(input("Number (1-9) : "))

        # check move
        if is_valid_move(grid, row, col, num):
            grid[row][col] = num
            print("Okay")
            print_grid(grid)
        else:
            print("Try again")

    print("Congratulations !")

if __name__ == "__main__":
    main()


