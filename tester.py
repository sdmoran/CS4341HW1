from ex1 import ConnectFour
from ex2 import isreverse
from ex3 import wordset
from ex3 import jaccard

class Tester:
    W = 7
    H = 6
    BOARD1 = [
        [1, 1, 1, 1, 2, 1, 0],
        [0, 2, 2, 2, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    BOARD2 = [
        [2, 1, 1, 1, 2, 1, 0],
        [0, 2, 2, 2, 0, 0, 0],
        [0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    BOARD3 = [
        [0, 0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]
    ]

    BOARD4 = [
        [0, 0, 0, 2, 2, 1, 0],
        [0, 0, 0, 0, 2, 2, 0],
        [0, 0, 0, 2, 1, 2, 0],
        [0, 0, 2, 0, 0, 1, 0],
        [0, 2, 0, 0, 0, 0, 1],
        [2, 0, 0, 0, 0, 0, 2]
    ]

    c = ConnectFour(BOARD1, W, H)

    b = ConnectFour(BOARD2, W, H)

    a = ConnectFour(BOARD3, W, H)

    d = ConnectFour(BOARD4, W, H)

    print("Outcome a:\n")
    a.printOutcome()

    print("Outcome b:\n")
    b.printOutcome()

    print("Outcome c:\n")
    c.printOutcome()

    print("Outcome d:\n")
    d.printOutcome()

    print(isreverse("d s a(", "(a s dd"))

    print("Jaccard: ")
    print(jaccard('glass_ascii.txt', 'alice_ascii.txt'))

