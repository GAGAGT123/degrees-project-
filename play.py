from tictactoe import initial_state, player, actions, result, winner, terminal, utility, minimax, X, O

def print_board(board):
    print("\n")
    for i, row in enumerate(board):
        print(" " + " | ".join([cell if cell is not None else " " for cell in row]))
        if i < 2:
            print("-----------")
    print("\n")

def main():
    board = initial_state()
    human = X
    computer = O if human == X else X
    
    print("Tic-Tac-Toe vs Computer!")
    print("You are playing as", human)
    print("Enter moves as two numbers: row then column (0 to 2)")
    print("Example: 1 2 means second row, third column\n")
    
    while not terminal(board):
        print_board(board)
        current = player(board)
        
        if current == human:
            while True:
                try:
                    move = input("Your move (row column): ").strip().split()
                    if len(move) != 2:
                        print("Enter two numbers only!")
                        continue
                    
                    action = (int(move[0]), int(move[1]))
                    
                    if action not in actions(board):
                        print("Invalid move! Cell occupied or out of range.")
                        continue
                    
                    break
                except ValueError:
                    print("Enter valid integers only!")
            
            board = result(board, action)
        
        else:
            print("Computer is thinking...")
            action = minimax(board)
            if action:
                board = result(board, action)
                print(f"Computer played at {action}")
    
    print_board(board)
    win = winner(board)
    
    if win == human:
        print("You win!")
    elif win == computer:
        print("Computer wins!")
    else:
        print("Tie!")

if __name__ == "__main__":
    main()
