# Initialisations
grid = [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]
grid_r = [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]


def restart():
    # Reset all values
    print("\n" * 10)
    print("New Game!\n\n")
    global grid, grid_r

    current_player = "O"
    grid = [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]
    grid_r = [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]

    show_grid()
    play(current_player)


def show_grid():
    # Draw lines and places the symbol in each tile
    print("     |     |     ")
    print(" ", grid[0][0], " | ", grid[0][1], " | ", grid[0][2])
    print("-----|-----|-----")
    print(" ", grid[1][0], " | ", grid[1][1], " | ", grid[1][2])
    print("-----|-----|-----")
    print(" ", grid[2][0], " | ", grid[2][1], " | ", grid[2][2])
    print("     |     |     ")


def play(current_player):
    # Tries and catches if input is not an integer from 1-9
    try:
        print("\nIt is now player " + current_player + "'s turn!\n")
        place = int(input("\nenter the tile you want to play (1-9)")) - 1
        # Divides and takes modulo to determine the x and y coordinates on the grid
        y = int(place / 3)
        x = int(place % 3)
        # Checks if the tile selected is empty
        if grid[y][x] == " ":

            grid[y][x] = current_player
            grid_r[2 - x][y] = current_player
        else:
            print("\nThere is already something in this tile!\n")
    except:
        print("\nInvalid input!\n")
    show_grid()
    victory_check(current_player)


def victory_check(current_player):
    # Checks for both players if there are any 3 Os or Xs in a row, horizontally, vertically or diagonally
    for i in range(3):
        if (grid[i] == ["O", "O", "O"]) or (grid_r[i] == ["O", "O", "O"]) or (
                grid[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O") or (
                grid_r[0][0] == "O" and grid[1][1] == "O" and grid[2][2] == "O"):
            print("Player O wins!")
            restart()

        if (grid[i] == ["X", "X", "X"]) or (grid_r[i] == ["X", "X", "X"]) or (
                grid[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X") or (
                grid_r[0][0] == "X" and grid[1][1] == "X" and grid[2][2] == "X"):
            print("Player X wins!")
            restart()

    # Changes turn between the players
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    # Given that all 9 tiles are filled with no victory, it is set as a tie
    if not any(" " in sublist for sublist in grid):
        print("Tie!")
        restart()

    # Calls play()
    play(current_player)


restart()