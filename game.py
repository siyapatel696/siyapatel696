
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board)):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False
class B:
    def one(self):
        s=0
        l=0
        self.s=s
        self.l=l

    def two(self):
        board = [[" " for _ in range(3)] for _ in range(3)]
        player = "X"
        turns = 0
        

        print("Welcome to Tic-Tac-Toe Game!")
        print_board(board)

        while turns < 9:
            row = int(input(f"Player {player}, enter row (1-3): ")) - 1
            col = int(input(f"Player {player}, enter column (1-3): ")) - 1

            if row < 0 or row > 2 or col < 0 or col > 2 or board[row][col] != " ":
                print("Invalid move. Try again.")
                continue
            board[row][col] = player
            print_board(board)

            if check_winner(board):
                print(f"Player {player} wins")
                if player=="O":
                    self.s+=1   
                else:
                    self.l+=1
                print('score:')
                print('O :',self.s,'X:',self.l)
                break
            
       

            if turns == 8:
                print("It's a tie!")
                break

            player = "O" if player == "X" else "X"
            
            turns += 1            
a1=B()
a1.one()
a1.two()
x=input("enter stop or play again")
while x=='play again':
    a1.two()
    x=input("enter stop or play again")
    





    

