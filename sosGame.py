
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
    self.gui.clear_error()
    self.mode = self.gui.selected_mode.get()
    self.gui.show_stuff()

  def current_symbol(self):
    return self.turn.symbol

  def place_move(self, i, j):
    if (i >= self.board.size or i < 0 or j >= self.board.size or j < 0):
      self.gui.display_error("Not a valid space")
      return
    if self.board.spaces[i][j]['text'] == '':
      self.gui.clear_error()
      self.board.set_move(i, j, self.current_symbol())
      self.change_turn()
    else:
      self.gui.display_error("Please pick unoccupied space")

  def change_turn(self):
    self.turn = self.players[1] if self.turn == self.players[0] else self.players[0]
    self.gui.display_turn()

class sosBoard:
  def __init__(self, game, size):
    self.game = game
    self.size = size
    self.spaces = [[None for _ in range(self.size)] for _ in range(self.size)]

  def select_size(self):
    new_size = int(self.game.gui.board_size_entry.get()) if self.game.gui.board_size_entry.get() != "" else 8
    if new_size > 2:
      self.game.gui.clear_board()
      self.game.gui.clear_error()
      self.size = new_size
      self.spaces = [[None for _ in range(self.size)] for _ in range(self.size)]
      self.game.gui.display_board()
      self.game.gui.show_stuff()
    else:
      self.game.gui.clear_board()
      self.game.gui.clear_error()
      self.size = 8
      self.spaces = [[None for _ in range(self.size)] for _ in range(self.size)]
      self.game.gui.display_board()
      self.game.gui.show_stuff()
      self.game.gui.display_error("Board size too small, must be 3 or more.")

  def set_move(self, i, j, symbol):
      self.spaces[i][j]['text'] = symbol.upper()


def main():
  root = tk.Tk()
  game = sosGame(root)
  root.mainloop()

main()
