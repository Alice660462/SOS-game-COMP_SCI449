
import tkinter as tk
from sosGUI import GameGUI

class Player:
  def __init__(self, color):
    self.color = color
    self.score = 0
    self.symbol = 'S'

  def change_symbol(self, symbol):
    self.symbol = symbol

  def get_score(self):
    return self.score

  def score_point(self):
    self.score += 1


class sosGame:
  def __init__(self, root):
    self.root = root
    self.mode = "Simple"
    self.players = [Player("Red"), Player("Blue")]
    self.turn = self.players[0]
    self.board = sosBoard(self, 0)
    self.gui = GameGUI(self, self.root)

  def select_mode(self):
    self.gui.clear_message()
    self.mode = self.gui.selected_mode.get()
    self.gui.show_stuff()

  def current_symbol(self):
    return self.turn.symbol

  def place_move(self, i, j):
    if (i >= self.board.size or i < 0 or j >= self.board.size or j < 0):
      self.gui.display_message("Error: Not a valid space")
      return
    if self.board.spaces[i][j]['text'] == '':
      self.gui.clear_message()
      self.board.set_move(i, j, self.current_symbol())
      self.score_sos(i, j)
      self.gui.display_scores()
      self.change_turn()
      if (self.detect_game_ended()):
        if (self.determine_winner() != 'tie'):
          self.gui.display_message(f"Congratulations! {self.determine_winner()} has won the game!")
        else:
          self.gui.display_message("The game has ended in a tie!")
        return
    else:
      self.gui.display_message("Error: Please pick unoccupied space")

  def change_turn(self):
    self.turn = self.players[1] if self.turn == self.players[0] else self.players[0]
    self.gui.display_turn()

  def score_sos(self, i, j):
    if self.board.spaces[i][j]['text'] == 'O':
      if i > 0 and j > 0 and i < self.board.size - 1 and j < self.board.size - 1 and self.board.spaces[i + 1][j + 1]['text'] == 'S' and self.board.spaces[i - 1][j - 1]['text'] == 'S':
        self.turn.score_point()
      if i > 0 and j > 0 and i < self.board.size - 1 and j < self.board.size - 1 and self.board.spaces[i + 1][j - 1]['text'] == 'S' and self.board.spaces[i - 1][j + 1]['text'] == 'S':
        self.turn.score_point()
      if j > 0 and j < self.board.size - 1 and self.board.spaces[i][j + 1]['text'] == 'S' and self.board.spaces[i][j - 1]['text'] == 'S':
        self.turn.score_point()
      if i > 0 and i < self.board.size - 1 and self.board.spaces[i + 1][j]['text'] == 'S' and self.board.spaces[i - 1][j]['text'] == 'S':
        self.turn.score_point()
    if self.board.spaces[i][j]['text'] == 'S':
      if i > 1 and j > 1 and i < self.board.size - 2 and j < self.board.size - 2 and self.board.spaces[i + 1][j + 1]['text'] == 'O' and self.board.spaces[i + 2][j + 2]['text'] == 'S':
        self.turn.score_point()
      if j > 1 and i < self.board.size - 2 and self.board.spaces[i + 1][j - 1]['text'] == 'O' and self.board.spaces[i + 2][j - 2]['text'] == 'S':
        self.turn.score_point()
      if j < self.board.size - 2 and self.board.spaces[i][j + 1]['text'] == 'O' and self.board.spaces[i][j + 2]['text'] == 'S':
        self.turn.score_point()
      if i < self.board.size - 2 and self.board.spaces[i + 1][j]['text'] == 'O' and self.board.spaces[i + 2][j]['text'] == 'S':
        self.turn.score_point()
      if i > 1 and j > 1 and self.board.spaces[i - 1][j - 1]['text'] == 'O' and self.board.spaces[i - 2][j - 2]['text'] == 'S':
        self.turn.score_point()
      if i > 1 and j < self.board.size - 2 and self.board.spaces[i - 1][j + 1]['text'] == 'O' and self.board.spaces[i - 2][j + 2]['text'] == 'S':
        self.turn.score_point()
      if j > 1 and self.board.spaces[i][j - 1]['text'] == 'O' and self.board.spaces[i][j - 2]['text'] == 'S':
        self.turn.score_point()
      if i > 1 and self.board.spaces[i - 1][j]['text'] == 'O' and self.board.spaces[i - 2][j]['text'] == 'S':
        self.turn.score_point()

  def detect_game_ended(self):
    if self.mode == 'Simple':
      if (self.players[1].score > 0 or self.players[0].score > 0 or self.board.is_board_full()):
        return True
      else:
        return False
    else:
      if (self.board.is_board_full()):
        return True
      else:
        return False

  def determine_winner(self):
    if (self.players[1].score > self.players[0].score):
      return self.players[1].color
    elif (self.players[1].score < self.players[0].score):
      return self.players[0].color
    else:
      return 'tie'

  def create_new_game(self):
    self.gui.clear_board()
    self.gui.clear_message()
    self.board.select_size()
    self.players[0].score = 0
    self.players[1].score = 0
    self.turn = self.players[0]
    self.gui.display_scores()
    self.gui.display_board()
    self.gui.show_stuff()

class sosBoard:
  def __init__(self, game, size):
    self.game = game
    self.size = size
    self.move_count = 0
    self.spaces = [[None for _ in range(self.size)] for _ in range(self.size)]

  def select_size(self):
    new_size = int(self.game.gui.board_size_entry.get()) if self.game.gui.board_size_entry.get() != "" else 8
    if new_size > 2:
#      self.game.gui.clear_board()
 #     self.game.gui.clear_message()
      self.size = new_size
      self.spaces = [[None for _ in range(self.size)] for _ in range(self.size)]
      self.move_count = 0
#      self.game.gui.display_board()
 #     self.game.gui.show_stuff()
    else:
 #     self.game.gui.clear_board()
  #    self.game.gui.clear_message()
      self.size = 8
      self.spaces = [[None for _ in range(self.size)] for _ in range(self.size)]
#      self.game.gui.display_board()
 #     self.game.gui.show_stuff()
      self.game.gui.display_message("Error: Board size too small, must be 3 or more.")

  def set_move(self, i, j, symbol):
      self.spaces[i][j]['text'] = symbol.upper()
      self.move_count += 1

  def is_board_full(self):
      return self.move_count >= self.size * self.size


def main():
  root = tk.Tk()
  game = sosGame(root)
  root.mainloop()

main()
