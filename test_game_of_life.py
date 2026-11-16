import unittest

from game_of_life import count_live_neighbours, next_cell_state, next_generation


def empty_board(width, height):
    return [[False] * width for _ in range(height)]


class NeighbourCountTests(unittest.TestCase):
    def setUp(self):
        self.full = [[True] * 4 for _ in range(4)]

    def test_corner_has_three_neighbours(self):
        for row, col in [(0, 0), (0, 3), (3, 0), (3, 3)]:
            self.assertEqual(count_live_neighbours(self.full, row, col), 3)

    def test_edge_has_five_neighbours(self):
        for row, col in [(0, 1), (1, 0), (3, 2), (2, 3)]:
            self.assertEqual(count_live_neighbours(self.full, row, col), 5)

    def test_inner_cell_has_eight_neighbours(self):
        self.assertEqual(count_live_neighbours(self.full, 1, 1), 8)

    def test_cell_does_not_count_itself(self):
        board = empty_board(3, 3)
        board[1][1] = True
        self.assertEqual(count_live_neighbours(board, 1, 1), 0)

    def test_no_wrap_around(self):
        board = empty_board(5, 5)
        board[0][4] = True  # opposite corner from (0, 0) if the board wrapped
        board[4][0] = True
        self.assertEqual(count_live_neighbours(board, 0, 0), 0)


class RuleTests(unittest.TestCase):
    def test_live_cell_rules(self):
        self.assertFalse(next_cell_state(True, 1))  # underpopulation
        self.assertTrue(next_cell_state(True, 2))
        self.assertTrue(next_cell_state(True, 3))
        self.assertFalse(next_cell_state(True, 4))  # overpopulation

    def test_dead_cell_rules(self):
        self.assertTrue(next_cell_state(False, 3))
        self.assertFalse(next_cell_state(False, 2))
        self.assertFalse(next_cell_state(False, 4))


class PatternTests(unittest.TestCase):
    def test_blinker_oscillates(self):
        horizontal = empty_board(5, 5)
        for col in (1, 2, 3):
            horizontal[2][col] = True
        vertical = empty_board(5, 5)
        for row in (1, 2, 3):
            vertical[row][2] = True

        self.assertEqual(next_generation(horizontal), vertical)
        self.assertEqual(next_generation(vertical), horizontal)

    def test_block_in_corner_is_stable(self):
        board = empty_board(4, 4)
        for row, col in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            board[row][col] = True
        self.assertEqual(next_generation(board), board)

    def test_lone_cell_dies(self):
        board = empty_board(3, 3)
        board[1][1] = True
        self.assertEqual(next_generation(board), empty_board(3, 3))

    def test_original_board_is_not_modified(self):
        board = empty_board(3, 3)
        board[1][1] = True
        next_generation(board)
        self.assertTrue(board[1][1])


if __name__ == "__main__":
    unittest.main()
