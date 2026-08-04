import csv
import random

grid = []

with open("grid.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        grid.append(row)

rows = len(grid)
cols = len(grid[0])

print("Grid Environment\n")

for row in grid:
    print(" ".join(row))

start_row = int(input("\nEnter Starting Row (0-4): "))
start_col = int(input("Enter Starting Column (0-4): "))

robot = [start_row, start_col]

reward = 0

dirt = 0

for row in grid:
    for cell in row:
        if cell == "D":
            dirt += 1

print("\nPolicies")
print("1. Random Policy")
print("2. Right-Down Policy")

choice = int(input("Choose Policy: "))

while dirt > 0:

    print("\nRobot Position:", robot)

    moves = []

    if robot[0] > 0:
        moves.append((-1,0))

    if robot[0] < rows-1:
        moves.append((1,0))

    if robot[1] > 0:
        moves.append((0,-1))

    if robot[1] < cols-1:
        moves.append((0,1))

    if choice == 1:
        move = random.choice(moves)

    else:

        if robot[1] < cols-1:
            move = (0,1)
        elif robot[0] < rows-1:
            move = (1,0)
        else:
            move = random.choice(moves)

    new_row = robot[0] + move[0]
    new_col = robot[1] + move[1]

    if grid[new_row][new_col] == "X":

        print("Obstacle Found")
        reward -= 1

    else:

        robot = [new_row,new_col]

        if grid[new_row][new_col] == "D":

            print("Dirt Cleaned")

            reward += 1

            dirt -= 1

            grid[new_row][new_col] = "."

        else:

            print("Moved")

print("\nCleaning Completed")

print("Total Reward =", reward)

print("\nFinal Grid")

for row in grid:
    print(" ".join(row))

with open("grid.csv","w",newline="") as file:

    writer = csv.writer(file)

    writer.writerows(grid)

print("\nGrid Saved Successfully.")
