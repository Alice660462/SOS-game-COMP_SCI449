import unittest
from unittest.mock import patch, MagicMock
import tkinter as tk
from sosGame import sosGame

class TestBoardSizeSelection(unittest.TestCase):

    def setUp(self):
        """This method runs before each test."""
        self.root = tk.Tk()
        self.game = sosGame(self.root)

    def tearDown(self):
        """Destroy the root window after each test."""
        self.root.destroy()

    # AC 1.1 Choose a valid board size
    @patch('tkinter.Entry.get', return_value = 6)
    def test_valid_board_size(self, mock_entry_get):
        """Test if valid board size is set correctly."""
        self.game.board.select_size()
        self.assertEqual(self.game.board.size, 6)

    # AC 1.2 Choose invalid small board size
    @patch('tkinter.Entry.get', return_value='2')
    def test_invalid_small_board_size(self, mock_entry_get):
        """Test if defaults to sixe 5 for invalid small board size."""
        self.game.board.select_size()  # invalid, size = 2
        self.assertEqual(self.game.board.size, 8)
        self.assertEqual(self.game.gui.error_label['text'], "Error: Board size too small, must be 3 or more.")
    # AC 1.3 Board size not chosen
    def test_default_board_size(self):
        """Test if the default board size is 8 when not chosen."""
        self.game.board.select_size()
        self.assertEqual(self.game.board.size, 8)

   # AC 2.1 Choose game mode
    @patch('tkinter.StringVar.get', return_value = 'General')
    def test_select_game_mode(self, mock_entry_get):
        """Test if game mode is set correctly."""
        self.game.select_mode()
        self.assertEqual(self.game.mode, "General")

   # AC 2.2 Test default game mode
    def test_default_game_mode(self):
        """Test if default board size is set correctly."""
        self.assertEqual(self.game.mode, "Simple")

   # AC 3.1 New game created with empty board of selected mode and board size
    def test_start_new_game(self):
        """Test if new game with defaults is created with empty board."""
        self.game.board.select_size()
        self.assertEqual(self.game.mode, "Simple")
        self.assertEqual(self.game.board.size, 8)
        self.assertEqual(self.game.turn.color, "Red")
        for i in range(self.game.board.size):
          for j in range(self.game.board.size):
            self.assertEqual(self.game.board.spaces[i][j]['text'], "")

   # AC 4.1 Make a valid move (simple)
    def test_make_simple_move(self):
        """Test if valid moves set spaces and change turns."""
        self.game.players[1].symbol = 'O'
        self.game.board.select_size()
        self.game.place_move(0,0)
        self.assertEqual(self.game.board.spaces[0][0]['text'], "S")
        self.assertEqual(self.game.turn.color, "Blue")
        self.game.place_move(0,1)
        self.assertEqual(self.game.board.spaces[0][1]['text'], "O")
        self.assertEqual(self.game.turn.color, "Red")

   # AC 4.2 Make an invalid move (simple)
    def test_make_invalid_simple_move(self):
        """Test if valid moves set spaces and change turns."""
        self.game.players[1].symbol = 'O'
        self.game.board.select_size()
        self.game.place_move(0,0)
        self.game.place_move(0,0)
        self.assertEqual(self.game.board.spaces[0][0]['text'], "S")
        self.assertEqual(self.game.turn.color, "Blue")
        self.assertEqual(self.game.gui.error_label['text'], "Error: Please pick unoccupied space")

   # AC 4.3 Make an invalid move outside board (simple)
    def test_make_out_of_bounds_simple_move(self):
        """Test if valid moves set spaces and change turns."""
        self.game.board.select_size()
        self.game.place_move(8,8)
        self.assertEqual(self.game.gui.error_label['text'], "Error: Not a valid space")
        self.assertEqual(self.game.turn.color, "Red")

   # AC 4.1 Make a valid move (general) (GPT written)
    def test_make_move_general(self):
        """Test if valid moves set spaces and change turns."""
        self.game.board.size = 3  # Set board size to 3 for testing
        self.game.board.spaces = [[{'text': ''} for _ in range(3)] for _ in range(3)]  # Mock board spaces
        self.game.mode = "General"

        # When I select a cell on the grid and place an 'S' in that cell
        self.game.place_move(0, 0)

        # Then the move should be registered
        self.assertEqual(self.game.board.spaces[0][0]['text'], 'S')

        # The current player's symbol should be displayed in the selected cell
        self.assertEqual(self.game.current_symbol(), 'S')

        # Check that the board state reflects the move
        expected_board = [
            [{'text': 'S'}, {'text': ''}, {'text': ''}],
            [{'text': ''}, {'text': ''}, {'text': ''}],
            [{'text': ''}, {'text': ''}, {'text': ''}]
        ]
        self.assertEqual(self.game.board.spaces, expected_board)

        # Ensure the turn has changed to the other player
        self.assertEqual(self.game.turn.color, 'Blue')

    def test_invalid_move(self):
        self.game.board.size = 3  # Set board size to 3 for testing
        self.game.board.spaces = [[{'text': ''} for _ in range(3)] for _ in range(3)]  # Mock board spaces

        self.game.mode = "General"
        self.game.place_move(0, 0)  # Make the first valid move
       # Attempt to place a move in an invalid position
        self.game.place_move(5, 5)  # Out of bounds
        self.assertEqual(self.game.board.spaces[0][0]['text'], 'S')  # The first move should still be there
        self.assertIn("Not a valid space", self.game.gui.error_label.cget("text"))

        # Attempt to place a move in the same cell
        self.game.place_move(0, 0)  # Should already be occupied
        self.assertIn("Please pick unoccupied space", self.game.gui.error_label.cget("text"))


if __name__ == '__main__':
    unittest.main()
