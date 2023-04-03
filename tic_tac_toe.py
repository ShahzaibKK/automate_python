import pprint as pp

the_board = {
    "top-L": "",
    "top-M": "",
    "top-R": "",
    "mid-L": "",
    "mid-M": "",
    "mid-R": "",
    "low-L": "",
    "low-M": "",
    "low-R": "",
}


def printboard(board):
    print(f"{board['top-L']}  |{board['top-M']}  |{board['top-R']}")
    print("- - - - -")
    print(f"{board['mid-L']}  |{board['mid-M']}  |{board['mid-R']}")
    print("- - - - -")
    print(f"{board['low-L']}  |{board['low-M']}  |{board['low-R']}")


# turn = "X"
# for i in range(9):
#     printboard(the_board)
#     print(f"turn for {turn}")
#     move = input()
#     the_board[move] = turn
#     if turn == "X":
#         turn = "O"
#     else:
#         turn = "X"

print(the_board)
pp.pprint(the_board)
print(pp.pformat(the_board))
