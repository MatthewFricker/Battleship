from random import choice

N_ROWS = 8
N_COLS = 8
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ships = {"A":"Aircraft Carrier", "B":"Battleship", "C":"Cruiser", "D":"Destroyer", "S":"Submarine"}
ship_hp = {"A":5,"B":4,"C":3,"S":3,"D":2}

def generateBoard():
    board = [[""]*N_COLS for _ in range(N_ROWS)]
    for ship in ship_hp:
        length = ship_hp[ship]
        is_vertical = choice([True, False])
        possible_places = []
        for i in range(N_ROWS):
            for j in range(N_COLS):
                if (is_vertical and i > N_ROWS - length) or (not is_vertical and j > N_COLS - length):
                    continue
                blocked = False
                for k in range(length):
                    if (is_vertical and board[i+k][j]) or (not is_vertical and board[i][j+k]):
                        blocked = True
                if not blocked:
                    possible_places.append((i,j))
        #print(length, possible_places)
        start_row, start_col = choice(possible_places)
        for l in range(length):
            if is_vertical:
                #print(start_row+l,start_col)
                board[start_row+l][start_col] = ship
            else:
                #print(start_row,start_col+l)
                board[start_row][start_col+l] = ship
    return board



def premadeBoard():
    return [["","","","","B","B","B","B"],
            ["A","","","","","","",""],
            ["A","","C","","","","",""],
            ["A","","C","","","","",""],
            ["A","","C","","","","",""],
            ["A","","","S","S","S","",""],
            ["","","","D","","","",""],
            ["","","","D","","","",""],
           ]

def printBoard(board):
    column_labels = ""
    for i in range(1, N_COLS+1):
        column_labels += f"\t|\t{i}"
    print(column_labels)
    for i, letter in enumerate(alphabet[:N_ROWS]):
        line = letter + "\t|\t"
        for j in range(N_COLS):
            line += board[i][j] + "\t|\t"
        print("-"*17*N_COLS)
        print(line)

def getCoords(attack_square):
    letters = {letter:i for i, letter in enumerate(alphabet[:N_ROWS])}
    if len(attack_square) < 2:
        print("Invalid entry. Try again:")
        return False
    row = attack_square[0].upper()
    col = attack_square[1:]
    if row not in letters:
        print("Invalid row. Try again:")
        return False
    try:
        col = int(col)
    except:
        print("Invalid column. Try again:")
        return False
    if col > N_COLS or col < 1:
        print("Invalid column. Try again:")
        return False
    return letters[row], col-1
        
        
def battleships():
    #enemy_board = premadeBoard()
    enemy_board = generateBoard()
    #printBoard(enemy_board)
    hits_board = [[""]*N_COLS for _ in range(N_ROWS)]
    printBoard(hits_board)
    sunk_ships = 0
    shots = 0
    while True:
        attack_square = input("Which square to attack? (-1 to quit)\t")
        if attack_square == "-1":
            break
        coord = getCoords(attack_square)
        if not coord:
            continue
        row, col = coord
        if hits_board[row][col]:
            print("That square has already been targeted")
            continue
        shots += 1
        if enemy_board[row][col]:
            hit_ship = enemy_board[row][col]
            ship_hp[hit_ship] -= 1
            result = "Hit!"
            if ship_hp[hit_ship] == 0:
                sunk_ships += 1
                result += f"\nYou sunk my {ships[hit_ship[0]]}!"
            hits_board[row][col] = "X"
        else:
            result = "Miss!"
            hits_board[row][col] = "-"
        
        printBoard(hits_board)
        print(result)
        print(f"Shots taken: {shots}")
        print(f"Ships sunk: {sunk_ships}")
        remaining_ships = [ships[s[0]] for s in ship_hp if ship_hp[s] != 0]
        if not remaining_ships:
            print("Sunk all ships!")
            break
        print("Remaining ships: " + ", ".join(remaining_ships))
    printBoard(enemy_board)



if __name__ == "__main__":
    #printBoard(generateBoard())
    battleships()
    
