def render_cell(board: list, x: int, y: int) -> str:
    """
    Render the specified cell from the game board as a string and return the string. The possible return values are 'X',
    'Y', or ' ' (empty). The origin of the board (0, 0) is the top left corner of the game board.

    :param board: The current game board.
    :type board: A list of n lists containing n characters (strings) each.
    :param x: x coordinate of the cell to render, with 0 being left-hand side of board.
    :type x: integer.
    :param y: y coordinate of the cell to render, with 0 being the top of the board.
    :type y: integer.
    :return: String representation of the contents of the cell ('X', 'O', or ' ').
    :rtype: String.
    """

    for row in board:
      for slot in row:
        print(f"{slot} |")
      print("_____________") 





test_board_2 = [[" ", "X"], ["O", " "]]
render_cell(test_board_2, 0, 0)









