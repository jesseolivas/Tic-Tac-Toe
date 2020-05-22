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

if cells[0] == "X" and cells[1] == "X" and cells[2] == "X":
    print("X wins")
elif cells[2] == "X" and cells[4] == "X" and cells[6] == "X":
    print("X wins")
elif cells[2] == "O" and cells[5] == "O" and cells[8] == "O":
    print("O wins")
else:
    while countc < 9:
        if cells[countc] == "X":
            countx += 1
        if cells[countc] == "O":
            counto += 1
        countc += 1
    if countx + counto >= 9:
        print("Draw")
    elif countx == 3 and counto == 3:
        print("Game not finished")

    else:
        print("Impossible")