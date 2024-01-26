# Write a function did_I_win_2_down that
# takes a player string and a two-dimensional 3 x 3 tic-tac-toe board as parameters and returns
# whether the player won with a column to the right.

def did_I_win_2_down(player, board):
    did_win = True
    for x in range(3): # for each row
        did_win &= player == [x][2]
    return did_win


did_I_win_2_down("X", [['0', '0', 'x'], \
                       ['0', 'x', '0'], \
                       ['x', '0', '0']])
