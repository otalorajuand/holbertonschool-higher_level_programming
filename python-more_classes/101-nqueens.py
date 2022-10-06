#!/usr/bin/python3
import sys

def NQueens(n):
    
    col = set()
    posDiag = set()
    negDiag = set()

    res = []
    board = []

    def backtrack(r):
        if r == n:
            copy = [row for row in board]
            res.append(copy)
            return
            
        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
                
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board.append([r, c])

            backtrack(r + 1)
                
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board.remove([r, c])
    backtrack(0)
    return res

for elem in NQueens(int(sys.argv[1])):
    print(elem)
