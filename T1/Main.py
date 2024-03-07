import os, time
os.system('cls')

mat = []
y = 1
x = 0
total = 0
currNum = ""
currDir = 1

def newTest(path):
    global mat
    mat = [[i for i in line[:-1]] for line in open(path)]

def newNum():
    global currNum, total
    try:
        int(mat[y][x])

        currNum += mat[y][x]

    except:
        if len(currNum) > 0:
            total += int(currNum)
            currNum = ""

        return


def moveR():
    global y, x, mat
    currPos = mat[y][x]
    newNum()
    match currPos:
        case "/": y-=1; return 4
        case "\\": y+=1; return 2
    x+=1
    return 1

def moveL():
    global y, x, mat
    currPos = mat[y][x]
    newNum()
    match currPos:
        case "/": y+=1; return 2
        case "\\": y-=1; return 4
    x-=1
    return 3

def moveU():
    global y, x, mat
    currPos = mat[y][x]
    newNum()
    match currPos:
        case "/": x+=1; return 1
        case "\\": x-=1; return 3
    y-=1
    return 4

def moveD():
    global y, x, mat
    currPos = mat[y][x]
    newNum()
    match currPos:
        case "/": x-=1; return 3
        case "\\": x+=1; return 1
    y+=1
    return 2

def runTest():
    global y, x, total, currNum
    y = 1
    x = 0
    total = 0
    currNum = ""
    currDir = 1
    
    start = time.process_time()

    while mat[y][x] != "#":
        match currDir:
            case 1: currDir = moveR()
            case 2: currDir = moveD()
            case 3: currDir = moveL()
            case 4: currDir = moveU()

    finish = time.process_time()

    print("A resposta {} foi achada em {} segundos.".format(total, start-finish))

def menu():
    os.system('cls')

    print("Select test case:")
    print("1) Width: 80, Height: 12")

    aux = int(input())

    currTest = "Input" + str((aux-1)) + ".txt"

    newTest(currTest)
    runTest()

menu()
