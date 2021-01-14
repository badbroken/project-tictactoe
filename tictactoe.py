def winner(array):
    try:
        # column check (For X)
        if ''.join(array[0]) == "XXX" or ''.join(array[1]) == "XXX" or ''.join(
                array[2]) == "XXX":
            print("X wins")
            exit()
        # column check (For O)
        elif ''.join(array[0]) == "OOO" or ''.join(array[1]) == "OOO" or ''.join(
                array[2]) == "OOO":
            print("O wins")
            exit()
        # row check (For X)
        elif ''.join([array[0][0], array[1][0], array[2][0]]) == "XXX" or ''.join(
                [array[0][1], array[1][1], array[2][1]]) == "XXX" or ''.join(
            [array[0][2], array[1][2], array[2][2]]) == "XXX":
            print("X wins")
            exit()
        # row check (For O)
        elif ''.join([array[0][0], array[1][0], array[2][0]]) == "OOO" or ''.join(
                [array[0][1], array[1][1], array[2][1]]) == "OOO" or ''.join(
            [array[0][2], array[1][2], array[2][2]]) == "OOO":
            print("O wins")
            exit()
        # Diagonal check (for X)
        elif ''.join([array[0][0], array[1][1], array[2][2]]) == "XXX" or ''.join(
                [array[0][2], array[1][1], array[2][0]]) == "XXX":
            print("X wins")
            exit()
        # Diagonal check (for O)
        elif ''.join([array[0][0], array[1][1], array[2][2]]) == "OOO" or ''.join(
                [array[0][2], array[1][1], array[2][0]]) == "OOO":
            print("O wins")
            exit()
    except TypeError:
        return


structured_move = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
print("---------")
print("| {} {} {} |".format(structured_move[0][0], structured_move[0][1], structured_move[0][2]))
print("| {} {} {} |".format(structured_move[1][0], structured_move[1][1], structured_move[1][2]))
print("| {} {} {} |".format(structured_move[2][0], structured_move[2][1], structured_move[2][2]))
print("---------")

coordinates_count = 1
while coordinates_count <= 9:
    print("Enter the coordinates:")
    coordinates = input().split()  # user_input_of_coordinates
    try:
        while int(coordinates[0]) > 3 or int(coordinates[0]) < 1 or int(coordinates[1]) > 3 or int(coordinates[1]) < 1:
            print("Coordinates should be from 1 to 3!")
            print("Enter the coordinates:")
            coordinates = input().split()
    except ValueError:
        print("You should enter numbers!")
        continue
    except IndexError:
        print("Please enter two coordinates")
        continue
    if structured_move[int(coordinates[0]) - 1][int(coordinates[1]) - 1] != "_":
        print("This cell is occupied! Choose another one!")
        continue
    if coordinates_count % 2 != 0:
        structured_move[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = 'X'
    else:
        structured_move[int(coordinates[0]) - 1][int(coordinates[1]) - 1] = 'O'
    print("---------")
    print("| {} {} {} |".format(structured_move[0][0], structured_move[0][1], structured_move[0][2]))
    print("| {} {} {} |".format(structured_move[1][0], structured_move[1][1], structured_move[1][2]))
    print("| {} {} {} |".format(structured_move[2][0], structured_move[2][1], structured_move[2][2]))
    print("---------")
    winner(structured_move)
    coordinates_count += 1

else:
    print("Draw")
