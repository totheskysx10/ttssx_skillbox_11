class Cell:
    def __init__(self, number):
        self.number = number
        self.is_occupied = False
        self.symbol = ' '

class Board:
    def __init__(self):
        self.cells = [Cell(i + 1) for i in range(9)]

    def display(self):
        for i in range(0, 9, 3):
            print(f"{self.cells[i].symbol} | {self.cells[i + 1].symbol} | {self.cells[i + 2].symbol}")
            if i < 6:
                print("---------")

    def change_cell_state(self, cell_number, symbol):
        cell = self.cells[cell_number - 1]
        if not cell.is_occupied:
            cell.symbol = symbol
            cell.is_occupied = True
            return True
        else:
            return False


    def check_game_end(self):
        for i in range(0, 9, 3):
            if self.cells[i].symbol == self.cells[i + 1].symbol == self.cells[i + 2].symbol != ' ':
                return True
            if self.cells[i // 3].symbol == self.cells[i // 3 + 3].symbol == self.cells[i // 3 + 6].symbol != ' ':
                return True

        if self.cells[0].symbol == self.cells[4].symbol == self.cells[8].symbol != ' ' or \
                self.cells[2].symbol == self.cells[4].symbol == self.cells[6].symbol != ' ':
            return True

        return all(cell.is_occupied for cell in self.cells)

class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0

    def make_move(self):
        try:
            move = int(input(f"{self.name}, введите номер клетки (1-9): "))
            if 1 <= move <= 9:
                return move
            else:
                print("Некорректный ввод. Введите число от 1 до 9.")
                return self.make_move()
        except ValueError:
            print("Некорректный ввод. Введите число от 1 до 9.")
            return self.make_move()

class Game:
    def __init__(self, player1, player2):
        self.board = Board()
        self.players = [player1, player2]
        self.current_player = None

    def start_turn(self):
        self.current_player = self.players[0] if self.current_player == self.players[1] else self.players[1]

    def play_turn(self):
        self.board.display()
        move = self.current_player.make_move()
        if self.board.change_cell_state(move, 'X' if self.current_player.name == 'Игрок 1' else 'O'):
            if self.board.check_game_end():
                self.board.display()
                print(f"{self.current_player.name} победил!")
                self.current_player.wins += 1
                return True
            return False
        else:
            print("Клетка уже занята. Попробуйте другую.")
            return self.play_turn()

    def play_game(self):
        while True:
            self.start_turn()
            if self.play_turn():
                break

        print(f"Счет: Игрок 1 - {self.players[0].wins}, Игрок 2 - {self.players[1].wins}")
        play_again = input("Хотите сыграть еще раз? (да/нет): ").lower()
        return play_again == 'да'

if __name__ == "__main__":
    player1 = Player("Игрок 1")
    player2 = Player("Игрок 2")
    game = Game(player1, player2)
    while game.play_game():
        pass