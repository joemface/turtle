

def main():
    grid =[[0] * 50 for i in range(50)]
    # 3 is right 4 is left
    # 2 is for down and means trail on, 1 for trail off
    # 5 is for saying move forward followed by amount of spaces
    direction = 'right'
    numOfSpaces = 0
    penToggle = 1
    row = 0
    col = 0
    userChoice = 0
    while(userChoice != '7'):
        userChoice = Menu()
        # python switch case
        match userChoice:
            case '1': penToggle = 1
            case '2': penToggle = 2
            case '3': 
                if direction == 'right':
                    direction = 'down'
                    
                elif direction == 'left':
                    direction = 'up'
                    
                elif direction == 'down':
                    direction = 'left'
               
                elif direction == 'up':
                    direction = 'right'
            case '4':
                if direction == 'right':
                    direction = 'up'
                    
                elif direction == 'left':
                    direction = 'down'
                    
                elif direction == 'down':
                    direction = 'right'
               
                elif direction == 'up':
                    direction = 'left'
            case '5':
                numOfSpaces = int(input("Enter number of spaces: "))
                if direction == 'down':
                    if penToggle == 1:
                        grid[row + numOfSpaces - 1][col ] = 1
                    else:
                        MoveDown(grid, row, col, numOfSpaces)
                    row += numOfSpaces - 1
                elif direction == 'up':
                    if penToggle == 1:
                        grid[(row - numOfSpaces) + 1][col ] = 1
                    else:
                        MoveUp(grid, row, col, numOfSpaces)
                    row = (row - numOfSpaces) + 1
                elif direction == 'left':
                    if penToggle == 1:
                        grid[row][(col - numOfSpaces) + 1] = 1
                    else:
                        MoveLeft(grid, row, col, numOfSpaces)
                    col = (col -numOfSpaces) + 1
                elif direction == 'right':
                    if penToggle == 1:
                        grid[row][col + numOfSpaces - 1] = 1
                    else:
                        MoveRight(grid, row, col, numOfSpaces)
                    col += numOfSpaces - 1
                    
            case '6':
                PrintGrid(grid)
            


def Menu():
    print("1. No trail")
    print("2. Trail On")
    print("3. Turn right")
    print("4. Turn left")
    print("5. Move Forward")
    print("6. Print Grid")
    print("7. Exit")

    choice = input("Enter your choice: ")
    return choice

def PrintGrid(grid):
    for i in range(50):
        for j in range(50):
            print(grid[i][j], end='  ')
        print("\n")

def MoveLeft(grid, row, col, amountOfSpaces):
    #             start         stop       increment
    for j in range(col, col-amountOfSpaces, -1):
        grid[row][j] = 1

def MoveRight(grid, row, col, amountOfSpaces):
    #             start         stop       increment
    for j in range(col, col + amountOfSpaces, 1):
        grid[row][j] = 1


def MoveUp(grid, row, col, amountOfSpaces):
    #             start         stop       increment
    for i in range(row, row - amountOfSpaces, -1):
        grid[i][col] = 1

def MoveDown(grid, row, col, amountOfSpaces):
    #             start         stop       increment
    for i in range(row, row + amountOfSpaces, 1):
        grid[i][col] = 1



main()