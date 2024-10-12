import tkinter as tk

class GameGUI:
  def __init__(self, game, root):
    self.game = game
    self.root = root
    self.root.title("SOS Game")


    self.create_window()

  def create_window(self):
    self.selected_mode = tk.StringVar(value="Simple")

    self.mode_label = tk.Label(self.root, text="Mode:")
    self.mode_label.grid(row=1, column=0)
    self.simple_radio = tk.Radiobutton(self.root, text="Simple", variable=self.selected_mode, value="Simple", command=self.game.select_mode)
    self.simple_radio.grid(row=1, column=1)
    self.general_radio = tk.Radiobutton(self.root, text="General", variable=self.selected_mode, value="General", command=self.game.select_mode)
    self.general_radio.grid(row=1, column=2)

    self.board_size_label = tk.Label(self.root, text="Board size:")
    self.board_size_label.grid(row=2, column=0)
    self.board_size_entry = tk.Entry(self.root, width=3)
    self.board_size_entry.grid(row=2, column=1)
    self.board_size_button = tk.Button(self.root, text="Submit", command=self.game.board.select_size)
    self.board_size_button.grid(row=2, column=2)

    self.state_label = tk.Label(self.root, text=f"Mode: {self.game.mode}, size: {self.game.board.size}")
    self.state_label.grid(row=3, column=0, columnspan=2)
    self.player_label = tk.Label(self.root, text=f"Player: {self.game.turn.color}")
    self.player_label.grid(row=3, column=2)

    self.selected_red_move = tk.StringVar(value="S")
    self.red_label = tk.Label(self.root, text="Red:")
    self.red_label.grid(row=4, column=0)
    self.red_s_radio = tk.Radiobutton(self.root, text="S", variable=self.selected_red_move, value="S", command=self.update_red_symbol)
    self.red_s_radio.grid(row=4, column=1)
    self.red_o_radio = tk.Radiobutton(self.root, text="O", variable=self.selected_red_move, value="O", command=self.update_red_symbol)
    self.red_o_radio.grid(row=4, column=2)

    self.selected_blue_move = tk.StringVar(value="S")
    self.blue_label = tk.Label(self.root, text="Blue:")
    self.blue_label.grid(row=5, column=0)
    self.blue_s_radio = tk.Radiobutton(self.root, text="S", variable=self.selected_blue_move, value="S", command=self.update_blue_symbol)
    self.blue_s_radio.grid(row=5, column=1)
    self.blue_o_radio = tk.Radiobutton(self.root, text="O", variable=self.selected_blue_move, value="O", command=self.update_blue_symbol)
    self.blue_o_radio.grid(row=5, column=2)

    self.error_label = tk.Label(self.root, text="")
    self.error_label.grid(row=6, column=0, columnspan=3)

    self.display_board()

  def show_stuff(self):
    self.state_label.config(text=f"Mode: {self.game.mode}, size: {self.game.board.size}")

  def display_turn(self):
    self.player_label.config(text=f"Player: {self.game.turn.color}")

  def display_error(self, error):
    self.error_label.config(text=f"Error: {error}")

  def clear_error(self):
    self.error_label.config(text=f"")

  def display_board(self):
    for i in range(self.game.board.size):
      for j in range(self.game.board.size):
        button = tk.Button(self.root, text ="", width=3, height=1, command=lambda i=i, j=j: self.game.place_move(i, j))
        button.grid(row=i, column=j+3)
        self.game.board.spaces[i][j] = button

  def clear_board(self):
    for i in range(self.game.board.size):
      for j in range(self.game.board.size):
        self.game.board.spaces[i][j].destroy()

  def update_red_symbol(self):
    self.game.players[0].change_symbol(self.selected_red_move.get())
  def update_blue_symbol(self):
    self.game.players[1].change_symbol(self.selected_blue_move.get())
