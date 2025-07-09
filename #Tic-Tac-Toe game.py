#Tic-Tac-Toe game

def welcome_message():
    print("Welcome to the Tic-Tac-Toe game!\n")

def menu():
    print("1. Play Game")
    print("2. Game Rules")
    print("3. Exit")

def game_rules():
    print("\nGame Rules:")
    print("1. The game is played on a 3x3 grid.")
    print("2. Players (or computers) take turns placing their mark (X or O) in an empty cell.")
    print("3. The first player to get three of their marks in a row (horizontally, vertically, or diagonally) wins.")
    print("4. If all cells are filled and no player has three in a row, the game is a draw.\n")


class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.player = 'X'
        self.computer = 'O'
        
    
    def display_board(self):
        print("Current Board:")
        
        print('-' * 9)
        for row in self.board:
            print(' | '.join(row))
            print('-' * 9)
    
    def make_move(self, row, col, player):
        if self.board[row][col] == ' ':
            if player == '1':
                self.board[row][col] = self.player
                return True
            elif player == '2':
                self.board[row][col] = self.computer
                return True
        else:
            print("Cell already taken. Try again.")
            return False

    def check_winner(self):

        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False
    
def main():
    welcome_message()
    player = '1'
    while True:
        menu()
        try:
            choice = input("Enter your choice (1-3): ")
            if choice not in ['1', '2', '3']:
                raise ValueError("Choice must be between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.\n")


        if choice == '1':
            break
        elif choice == '2':
            game_rules()
        elif choice == '3':
            print("Thank you for playing! Goodbye!")
            return

    print("Starting the game...\n")

    contine_playing = True

    while contine_playing:
        game = TicTacToe()
        game.display_board()
        while True:
            try:
                row = int(input(f"Player {player} enter the row (1-3) for your move: "))
                if row < 1 or row > 3:
                    raise ValueError("Row values must be between 1 and 3.") 
                col = int(input(f"Player {player} enter the colum (1-3) for your move: "))
                if col < 1 or col > 3:
                    raise ValueError("Column values must be between 1 and 3.")
            except Exception as e:
                print(f"Invalid input: {e} Please try again.")
                continue
            if game.make_move(row - 1, col - 1, player):
                game.display_board()
                if game.check_winner():
                    print(f"Player {player} wins!")
                    break
                if all(cell != ' ' for row in game.board for cell in row):
                    print("It's a draw!")
                    break
                if player == '1':
                    player = '2'
                else:
                    player = '1'
                print(f"It is now Player {player}'s turn.")
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            contine_playing = False
            print("Thank you for playing! Goodbye!")
        

if __name__ == "__main__":
    main()