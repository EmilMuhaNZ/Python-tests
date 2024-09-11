def main():
    grid = input("Please enter a string representing TicTacToe grid: ")
    player1 = "X"
    player2 = "O"
    print("TicTacToe Grid:")
    print("")
    print_grid(grid)
    print("")
    print(f"Player X has won: {check_win(grid, player1)}")
    print(f"Player O has won: {check_win(grid, player2)}")


def print_grid(grid):
    print(f"{grid[0]}|{grid[1]}|{grid[2]}")
    print("-----")
    print(f"{grid[3]}|{grid[4]}|{grid[5]}")
    print("-----")
    print(f"{grid[6]}|{grid[7]}|{grid[8]}")



def check_win(grid, player):
    player_check = player * 3
    player_win = False
    
    for item in get_rows(grid):
        if item == player_check:
            player_win = True
            
    for item in get_columns(grid):
        if item == player_check:
            player_win = True
            
    for item in get_diagonals(grid):
        if item == player_check:
            player_win = True
            
    return player_win

def get_rows(grid):
    row_1 = grid[0] + grid[1] + grid[2]
    row_2 = grid[3] + grid[4] + grid[5]
    row_3 = grid[6] + grid[7] + grid[8]
    row_list = [row_1, row_2, row_3]
    return row_list

def get_columns(grid):
    column_1 = grid[0] + grid[3] + grid[6]
    column_2 = grid[1] + grid[4] + grid[7]
    column_3 = grid[2] + grid[5] + grid[8]
    column_list = [column_1, column_2, column_3]
    return column_list

def get_diagonals(grid):
    diagonal_1 = grid[0] + grid[4] + grid[8]
    diagonal_2 = grid[2] + grid[4] + grid[6]
    diagonal_list = [diagonal_1, diagonal_2]
    return diagonal_list