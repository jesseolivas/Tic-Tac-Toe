# write your code here
cells = list(input("Enter cells: "))
print("---------")
print("| " + cells[0] + " " + cells[1] + " " + cells[2] + " |")
print("| " + cells[3] + " " + cells[4] + " " + cells[5] + " |")
print("| " + cells[6] + " " + cells[7] + " " + cells[8] + " |")
print("---------")
countx = 0
counto = 0
counts = 0
countc = 0

if (cells[0] and cells[1] and cells[2] == "X") or (cells[2] and cells[4] and cells[6] == "X"):
    print("X wins")
elif cells[2] and cells[5] and cells[8] == "O":
    print("O wins")
else:
    while countc < 9:
        if cells[countc] == "X":
            countx += 1
        if cells[countc] == "O":
            counto += 1
        countc += 1
    if countx + countc == 9:
        print("Draw")
    else:
        print("Game not finished")
    if (cells[0] and cells[3] and cells[6] == "X") and (cells[1] and cells[4] and cells[7] == "O"):
        print("Impossible")