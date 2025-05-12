from typing import List

class Solution:
    def isValidSudoku(board: List[List[str]]) -> bool:
        count = [0] * 9
        print(count)

        currLimit = 3

        print("3X3 TEST:")
        while currLimit <= len(board): # checks all 3x3's
            for i in range(len(board)): #row
                for j in range(currLimit-3, currLimit): #col by 3 cells each
                    if (board[i][j] != "."): # if an actual num is read
                        count[int(board[i][j]) - 1] += 1 # count 1 instance of num
                        if count[int(board[i][j]) - 1] > 1: # if count > 1
                            print("RETURN FALSE")
                            print(f"num: {board[i][j]}, j: {j}, i: {i}, count: {count}, currLimit: {currLimit}")
                            return False
                    print(f"num: {board[i][j]}, j: {j}, i: {i}, count: {count}, currLimit: {currLimit}")

                if i == 3 or i == 6 or i == 9: # if done checking 3x3,
                    print("RESET")
                    count = [0] * 9 # reset counter
            currLimit += 3

        count = [0] * 9
        print("ROWS N COLS TEST:")
        for i in range(len(board)):
            for j in range(len(board)):
                if (board[i][j] != "."): # if an actual num is read
                    count[int(board[i][j]) - 1] += 1 # count 1 instance of num
                    if count[int(board[i][j]) - 1] > 1: # if count > 1
                        print("RETURN FALSE")
                        print(f"num: {board[i][j]}, j: {j}, i: {i}, count: {count}, currLimit: {currLimit}")
                        return False
                print(f"num: {board[i][j]}, j: {j}, i: {i}, count: {count}, currLimit: {currLimit}")

        print("Is Valid: TRUE")
        return True

Solution.isValidSudoku(
[["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","8",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]])