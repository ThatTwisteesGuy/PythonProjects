
def restart():
    # Reset all values
    print("\n" * 10)
    print("New Game!\n\n")
    global grid

    counts = [0, 0, 0, 0, 0, 0, 0]
    current_player = "O"
    grid = [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "], [" ", " ", " ", " ", " ", " "],[" ", " ", " ", " ", " ", " "]

    show_display()
    play(current_player, counts)


def show_display():
    for i in range(6):
        for x in range(7):
            print(" ", grid[x][5-i], " |", end="")
        print("")
        for x in range(7):
            print("-----|", end="")
        print("")


def play(current_player, counts):
    placement = int(input("Enter the column you want to drop in"))
    if counts[placement] <= 5:
        grid[placement][counts[placement]] = current_player
        counts[placement] = counts[placement]+1
    else:
        print("That column is not available")
    victory_check(current_player, counts, placement)


def victory_check(current_player, counts, placement):
    show_display()
    current_location = [placement, counts[placement]-1]
    total1 = check_angle_0(current_location, current_player)
    total2 = check_angle_1(current_location, current_player)
    total3 = check_angle_2(current_location, current_player)
    total4 = check_angle_3(current_location, current_player)

    truetotal = max(total1, total2, total3, total4)
    if (truetotal >= 4):
        print("Player "+current_player+" Wins!")
        restart()

    current_player = "X" if current_player == "O" else "O"
    play(current_player, counts)

def check_angle_0(current_location, current_player):
    new_location = [0,0]
    new_location[0] = current_location[0]
    new_location[1] = current_location[1]
    total_linked = 1

    for i in range(4):
        try:
            new_location[1] = new_location[1]-1
            new_location[0] = new_location[0]
            #print(new_location)

            if grid[new_location[0]][new_location[1]] == current_player:
                total_linked = total_linked + 1
            else:
                break
        except:
            break

    #print(total_linked)
    print(current_location)
    return total_linked

def check_angle_1(current_location, current_player):
    new_location = [0,0]
    new_location[0] = current_location[0]
    new_location[1] = current_location[1]
    total_linked = 1

    for i in range(4):
        try:
            new_location[1] = new_location[1] + 1
            new_location[0] = new_location[0] + 1
            #print(new_location)

            if grid[new_location[0]][new_location[1]] == current_player:
                total_linked = total_linked + 1
            else:
                break
        except:
            break

    new_location[0] = current_location[0]
    new_location[1] = current_location[1]

    for i in range(4):
        try:
            new_location[1] = new_location[1] - 1
            new_location[0] = new_location[0] - 1
            #print(new_location)

            if grid[new_location[0]][new_location[1]] == current_player:
                total_linked = total_linked + 1
            else:
                break
        except:
            break

    #print(total_linked)
    print(current_location)
    return total_linked

def check_angle_2(current_location, current_player):
    new_location = [0,0]
    new_location[0] = current_location[0]
    new_location[1] = current_location[1]
    total_linked = 1

    for i in range(4):
        try:
            new_location[1] = new_location[1] + 0
            new_location[0] = new_location[0] + 1
            #print(new_location)

            if grid[new_location[0]][new_location[1]] == current_player:
                total_linked = total_linked + 1
            else:
                break
        except:
            break

    new_location[0] = current_location[0]
    new_location[1] = current_location[1]

    for i in range(4):
        try:
            new_location[1] = new_location[1] - 0
            new_location[0] = new_location[0] - 1
            #print(new_location)

            if grid[new_location[0]][new_location[1]] == current_player:
                total_linked = total_linked + 1
            else:
                break
        except:
            break

    #print(total_linked)
    print(current_location)
    return total_linked


def check_angle_3(current_location, current_player):
    new_location = [0,0]
    new_location[0] = current_location[0]
    new_location[1] = current_location[1]
    total_linked = 1

    for i in range(4):
        try:
            new_location[1] = new_location[1] - 1
            new_location[0] = new_location[0] + 1
            #print(new_location)

            if grid[new_location[0]][new_location[1]] == current_player:
                total_linked = total_linked + 1
            else:
                break
        except:
            break

    new_location[0] = current_location[0]
    new_location[1] = current_location[1]

    for i in range(4):
        try:
            new_location[1] = new_location[1] + 1
            new_location[0] = new_location[0] - 1
            #print(new_location)

            if grid[new_location[0]][new_location[1]] == current_player:
                total_linked = total_linked + 1
            else:
                break
        except:
            break

    #print(total_linked)
    print(current_location)
    return total_linked

restart()
