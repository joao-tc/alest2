import os, time
os.system('cls')

mat = []
y = -1
x = 0
total = 0
currNum = ""
currDir = 1

def newTest(path):
    global mat, y
    mat = [[i for i in line[:-1]] for line in open(path)]

    for i in range(len(mat)): 
        if mat[i][0] == "-": y = i; break


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

    print("The value {} was found in {} seconds.\n".format(total, finish-start))

def runAllTests():
    os.system('cls')

    for i in range(9):
        print("Case {}:".format(i+1))
        currTest = "Input" + str(i) + ".txt"
        newTest(currTest)
        runTest()

def menu():
    os.system('cls')

    print("Select test case:")
    print("0) exit\n1) 80x12\n2) 50x50\n3) 100x100\n4) 200x200\n5) 500x500\n6) 750x750\n7) 1000x1000\n8) 1500x1500\n9) 2000x2000\n10) Run all")

    aux = int(input())

    if aux == 0: return
    if aux == 10: runAllTests(); return

    currTest = "Input" + str((aux-1)) + ".txt"

    newTest(currTest)
    runTest()

    print("Enter to test again.")
    input()
    menu()

menu()
