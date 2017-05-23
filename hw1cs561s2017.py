import copy
import sys

class Point:
    x = -1
    y = -1

class Node:
    'the main node class'
    depth = 0
    alpha = -9999
    beta = 9999
    value = -9999
    x = -1
    y = -1
    nextX = -1
    nextY = -1
    board = [['*' for x in range(8)] for y in range(8)]
    flag=False

def printRef():
    for i in range(0,8):
        for j in range(0,8):
            print "(",i,",",j,")",
            print "\t",
        print
    return

def pr(x,y):
    y = x + 1
    x = y
    #print x,y,"in pr"
    if y == 0 :
        print "root",
    elif y==-1 or x==-2:
        print "pass",
    else:
        if x == 0:
            print "a",
        elif x == 1:
            print "b",
        elif x == 2:
            print "c",
        elif x == 3:
            print "d",
        elif x == 4:
            print "e",
        elif x == 5:
            print "f",
        elif x == 6:
            print "g",
        elif x == 7:
            print "h",
        print "%d" % y,
    print ",",
    return

def printLine1(node):
    #f = open("output.txt",'a')
    y = node.x + 1
    x = node.y
    if y == 0 or x == -1:
        print "root",
    elif y==-1 or x==-2:
        print "pass",
    else:
        if x == 0:
            print "a",
        elif x == 1:
            print "b",
        elif x == 2:
            print "c",
        elif x == 3:
            print "d",
        elif x == 4:
            print "e",
        elif x == 5:
            print "f",
        elif x == 6:
            print "g",
        elif x == 7:
            print "h",
        print "%d" % y,
    print ",",
    print "%d" %node.depth,
    print ",",

    if node.value == 9999:
        print "Infinity",
    elif node.value == -9999:
        print "-Infinity",
    else:
        print "%d" % node.value,
    print ",",

    if node.alpha == 9999:
        print "Infinity",
    elif node.alpha == -9999:
        print "-Infinity",
    else:
        print "%d" % node.alpha,
    print ",",

    if node.beta == 9999:
        print "Infinity"
    elif node.beta == -9999:
        print "-Infinity"
    else:
        print "%d" % node.beta
    return

def printLine(node):
    f = open("output.txt",'a')
    y = node.x + 1
    x = node.y
    if y == 0 or x == 0:
        f.write("root")
    elif y==-1 or x==-2:
        f.write("pass")
    else:
        if x == 0:
            f.write("a")
        elif x == 1:
            f.write("b")
        elif x == 2:
            f.write("c")
        elif x == 3:
            f.write("d")
        elif x == 4:
            f.write("e")
        elif x == 5:
            f.write("f")
        elif x == 6:
            f.write("g")
        elif x == 7:
            f.write("h")
        f.write("%d" % y)
    f.write(",")
    f.write("%d" %node.depth)
    f.write(",")

    if node.value == 9999:
        f.write("Infinity")
    elif node.value == -9999:
        f.write("-Infinity")
    else:
        f.write("%d" % node.value)
    f.write(",")

    if node.alpha == 9999:
        f.write("Infinity")
    elif node.alpha == -9999:
        f.write("-Infinity")
    else:
        f.write("%d" % node.alpha)
    f.write(",")

    if node.beta == 9999:
        f.write("Infinity")
    elif node.beta == -9999:
        f.write("-Infinity")
    else:
        f.write("%d" % node.beta)
    f.write("\n")
    f.close();
    return

def printBoard(board):
    for i in range(0,8):
        for j in range(0,8):
            print board[i][j],
            print "\t",
        print
    return


def numberOfX(board):
    count = 0
    for i in range(0,8):
        for j in range(0,8):
            if board[i][j] == 'X':
                count = count + 1
    return count

def numberOfO(board):
    count = 0
    for i in range(0,8):
        for j in range(0,8):
            if board[i][j] == 'O':
                count = count + 1
    return count

def isValidMove(board, x, y, turn):
    kas = copy.copy(board)
    noofX = numberOfX(board)
    noofO = numberOfO(board)
    board[x][y] = turn
    if turn == 'X':
        for i in range(x+1,8):
            if board[i][y] == '*':
                break;
            elif board[i][y] == 'X':
                for kk in range(x+1,i):
                    board[kk][y] = 'X'
                break

        for i in range(y+1,8):
            if board[x][i] == '*':
                break;
            elif board[x][i] == 'X':
                for kk in range(y+1,i):
                    board[x][kk] = 'X'
                break


        for i in range(y-1,0,-1):
            if board[x][i] == '*':
                break;
            elif board[x][i] == 'X':
                for kk in range(y-1,i,-1):
                    board[x][kk] = 'X'
                break

        for i in range(x-1,0,-1):
            if board[i][y] == '*':
                break;
            elif board[i][y] == 'X':
                for kk in range(x-1,i,-1):
                    board[kk][y] = 'X'
                break

        j = y
        for i in range(x+1,8):
            j = j + 1
            if j == 8:
                break
            if board[i][j] == '*':
                break
            elif board[i][j] == 'X':
                j = y
                for kk in range(x+1,i):
                    j = j + 1
                    board[kk][j] = 'X'
                break
            
        j = y
        for i in range(x+1,8):
            j = j - 1
            if j == -1:
                break  
            if board[i][j] == '*':
                break
            elif board[i][j] == 'X':
                j = y
                for kk in range(x+1,i):
                    j = j - 1
                    board[kk][j] = 'X'
                break
                  
        j = y
        for i in range(x-1,0,-1):
            j = j - 1
            if j == -1:
                break
            if board[i][j] == '*':
                break;
            elif board[i][j] == 'X':
                j = y
                for kk in range(x-1,i,-1):
                    j = j - 1
                    board[kk][j] = 'X'
                break
            
        j = y
        for i in range(x-1,0,-1):
            j = j + 1
            if j == 8:
                break
            if board[i][j] == '*':
                break;
            elif board[i][j] == 'X':
                j = y
                for kk in range(x-1,i,-1):
                    j = j + 1
                    board[kk][j] = 'X'
                break
            


        #printBoard(board)
    elif turn == 'O':  
        for i in range(x+1,8):
            if board[i][y] == '*':
                break;
            elif board[i][y] == 'O':
                for kk in range(x+1,i):
                    board[kk][y] = 'O'
                break

        for i in range(y+1,8):
            if board[x][i] == '*':
                break;
            elif board[x][i] == 'O':
                for kk in range(y+1,i):
                    board[x][kk] = 'O'
                break


        for i in range(y-1,0,-1):
            if board[x][i] == '*':
                break;
            elif board[x][i] == 'O':
                for kk in range(y-1,i,-1):
                    board[x][kk] = 'O'
                break

        for i in range(x-1,0,-1):
            if board[i][y] == '*':
                break;
            elif board[i][y] == 'O':
                for kk in range(x-1,i,-1):
                    board[kk][y] = 'O'
                break

        j = y
        for i in range(x+1,8):
            j = j + 1
            if j == 8:
                break
            if board[i][j] == '*':
                break
            elif board[i][j] == 'O':
                j = y
                for kk in range(x+1,i):
                    j = j + 1
                    board[kk][j] = 'O'
                break
            
        j = y
        for i in range(x+1,8):
            j = j - 1
            if j == -1:
                break  
            if board[i][j] == '*':
                break
            elif board[i][j] == 'O':
                j = y
                for kk in range(x+1,i):
                    j = j - 1
                    board[kk][j] = 'O'
                break
                  
        j = y
        for i in range(x-1,0,-1):
            j = j - 1
            if j == -1:
                break
            if board[i][j] == '*':
                break;
            elif board[i][j] == 'O':
                j = y
                for kk in range(x-1,i,-1):
                    j = j - 1
                    board[kk][j] = 'O'
                break
            
        j = y
        for i in range(x-1,0,-1):
            j = j + 1
            if j == 8:
                break
            if board[i][j] == '*':
                break;
            elif board[i][j] == 'O':
                j = y
                for kk in range(x-1,i,-1):
                    j = j + 1
                    board[kk][j] = 'O'
                break
    if noofX == numberOfX(board):
        board=copy.copy(kas)
        return False
    if noofO == numberOfO(board):
        board=copy.copy(kas)
        return False
    board=copy.copy(kas)
    return True


def numberOfChances(board1, turn):
    count = 0
    initScore = calcScore(board1, turn, 8, 8)
    for i in range(0, 8):
        for j in range(0, 8):
            if board1[i][j] != '*':
                continue
            else:
                kast = copy.deepcopy(board1)
                if isValidMove(kast, i, j, turn):
                    count=count+1
    #print count,"anything"
    #print turn,"ntng"
    p =  []
    for i in range(0, 8):
        for j in range(0, 8):
            if board1[i][j] != '*':
                continue
            kst = copy.deepcopy(board1)
            if isValidMove(kst, i, j, turn):
  #              print i," ******************************* ",j
                pp = Point()
                if len(p) == 0:
                    p = [Point()]
                    pp.x = i
                    pp.y = j
                    p[0] = pp
                else:
                    pp.x = i
                    pp.y = j
                    p.append(pp)
    return p

def calcScore(board1, turn, n, m):
    scrboard = [[0 for x in range(8)] for y in range(8)]
    scrboard[0][0] = 99
    scrboard[0][1] = -8
    scrboard[0][2] = 8
    scrboard[0][3] = 6
    scrboard[1][0] = -8
    scrboard[1][1] = -24
    scrboard[1][2] = -4
    scrboard[1][3] = -3
    scrboard[2][0] = 8
    scrboard[2][1] = -4
    scrboard[2][2] = 7
    scrboard[2][3] = 4
    scrboard[3][0] = 6
    scrboard[3][1] = -3
    scrboard[3][2] = 4
    scrboard[3][3] = 0
    for x in range(4, 8):
        for y in range(0, 4):
            scrboard[x][y] = scrboard[7 - x][y]
    for x in range(4, 8):
        for y in range(4, 8):
            scrboard[x][y] = scrboard[7 - x][7 - y]
    for x in range(0, 4):
        for y in range(4, 8):
            scrboard[x][y] = scrboard[x][7 - y]
    finscore = 0
    i = 0
    j = 0
    if turn == 'X':
        for i in range(0, n):
            for j in range(0, m):
                if board1[i][j] == 'X':
                    finscore = finscore + scrboard[i][j]
                elif board1[i][j] == 'O':
                    finscore = finscore - scrboard[i][j]
    elif turn == 'O':
        for i in range(0, n):
            for j in range(0, m):
                if board1[i][j] == 'O':
                    finscore = finscore + scrboard[i][j]
                elif board1[i][j] == 'X':
                    finscore = finscore - scrboard[i][j]
    return finscore
def modifyX(board, x, y):
    if x==-1 or y == -1:
        return
    board[x][y] = 'X'
    for i in range(x+1,8):
        if board[i][y] == '*':
            break;
        elif board[i][y] == 'X':
            for kk in range(x+1,i):
                board[kk][y] = 'X'
            break

    for i in range(y+1,8):
        if board[x][i] == '*':
            break;
        elif board[x][i] == 'X':
            for kk in range(y+1,i):
                board[x][kk] = 'X'
            break


    for i in range(y-1,0,-1):
        if board[x][i] == '*':
            break;
        elif board[x][i] == 'X':
            for kk in range(y-1,i,-1):
                board[x][kk] = 'X'
            break

    for i in range(x-1,0,-1):
        if board[i][y] == '*':
            break;
        elif board[i][y] == 'X':
            for kk in range(x-1,i,-1):
                board[kk][y] = 'X'
            break

    j = y
    for i in range(x+1,8):
        j = j + 1
        if j == 8:
            break
        if board[i][j] == '*':
            break
        elif board[i][j] == 'X':
            j = y
            for kk in range(x+1,i):
                j = j + 1
                board[kk][j] = 'X'
            break
        
    j = y
    for i in range(x+1,8):
        j = j - 1
        if j == -1:
            break  
        if board[i][j] == '*':
            break
        elif board[i][j] == 'X':
            j = y
            for kk in range(x+1,i):
                j = j - 1
                board[kk][j] = 'X'
            break
              
    j = y
    for i in range(x-1,0,-1):
        j = j - 1
        if j == -1:
            break
        if board[i][j] == '*':
            break;
        elif board[i][j] == 'X':
            j = y
            for kk in range(x-1,i,-1):
                j = j - 1
                board[kk][j] = 'X'
            break
        
    j = y
    for i in range(x-1,0,-1):
        j = j + 1
        if j == 8:
            break
        if board[i][j] == '*':
            break;
        elif board[i][j] == 'X':
            j = y
            for kk in range(x-1,i,-1):
                j = j + 1
                board[kk][j] = 'X'
            break
    return

def modifyY(board, x, y):
    if x==-1 or y == -1:
        return
    board[x][y] = 'O'
    for i in range(x+1,8):
        if board[i][y] == '*':
            break;
        elif board[i][y] == 'O':
            for kk in range(x+1,i):
                board[kk][y] = 'O'
            break

    for i in range(y+1,8):
        if board[x][i] == '*':
            break;
        elif board[x][i] == 'O':
            for kk in range(y+1,i):
                board[x][kk] = 'O'
            break


    for i in range(y-1,0,-1):
        if board[x][i] == '*':
            break;
        elif board[x][i] == 'O':
            for kk in range(y-1,i,-1):
                board[x][kk] = 'O'
            break

    for i in range(x-1,0,-1):
        if board[i][y] == '*':
            break;
        elif board[i][y] == 'O':
            for kk in range(x-1,i,-1):
                board[kk][y] = 'O'
            break

    j = y
    for i in range(x+1,8):
        j = j + 1
        if j == 8:
            break
        if board[i][j] == '*':
            break
        elif board[i][j] == 'O':
            j = y
            for kk in range(x+1,i):
                j = j + 1
                board[kk][j] = 'O'
            break
        
    j = y
    for i in range(x+1,8):
        j = j - 1
        if j == -1:
            break  
        if board[i][j] == '*':
            break
        elif board[i][j] == 'O':
            j = y
            for kk in range(x+1,i):
                j = j - 1
                board[kk][j] = 'O'
            break
              
    j = y
    for i in range(x-1,0,-1):
        j = j - 1
        if j == -1:
            break
        if board[i][j] == '*':
            break;
        elif board[i][j] == 'O':
            j = y
            for kk in range(x-1,i,-1):
                j = j - 1
                board[kk][j] = 'O'
            break
        
    j = y
    for i in range(x-1,0,-1):
        j = j + 1
        if j == 8:
            break
        if board[i][j] == '*':
            break;
        elif board[i][j] == 'O':
            j = y
            for kk in range(x-1,i,-1):
                j = j + 1
                board[kk][j] = 'O'
            break
    return

def boardtostring(board):
    bts = ""
    for i in range(0,8):
        for j in range(0,8):
            bts=bts+"%c" % board[i][j]
        bts = bts + "\n"
    return bts

SIZE = 8
board = [['*' for x in range(SIZE)] for y in range(SIZE)]
f = open("input1.txt",'r')
#print f.read()
turn = f.readline()[0]
if turn == 'X':
    turn1 = 'O'
else:
    turn1 = 'X'
findepth = ord(f.readline()[0]) - ord("0")
for i in range(0,8):
    line = f.readline()
    for j in range(0,8):
        board[i][j] = line[j]
f.close()
node = Node()
node.board = copy.deepcopy(board)
node.depth = 0
node.x = -1
node.y = -1

def ALPHA_BETA(node):
    node.nextX = -1
    node.nextY = -1
    f = open("output.txt",'w')
    f.write("Node,Depth,Value,Alpha,Beta\n")
    f.close()
    node=MAX_VALUE(node)
    if turn == 'X':
        modifyX(node.board,node.nextX,node.nextY)
    else:
        modifyY(node.board, node.nextX, node.nextY)
    f = open("output.txt",'r')
    datainfile = f.read()
    f.close()
    f = open("output.txt",'w')
    f.write(boardtostring(node.board))
    f.write(datainfile)
    f.close()
    return

def MAX_VALUE(node):
    if node.depth>findepth:
        node.value=calcScore(node.board,turn,8,8)
        return node
    if len(numberOfChances(node.board,turn))==0:
        #print "pass ",node.depth,node.value,node.alpha,node.beta
        printLine(node)
        #print " i called printline"
        #print "608"
        child=Node()
        child.flag=True
        tempBoard = copy.deepcopy(node.board)
        child.board=tempBoard
        child.depth=node.depth+1
        child.x=-2
        child.y=-2
        if node.flag==True:
            child.value=calcScore(child.board,turn,8,8)
            #print "i calculated score ",child.value
            child.x=-2
            child.y=-2
            printLine(child)
            node.value=child.value
            node.alpha=child.value
            printLine(node)
            return child
        #printLine(node)
        child=MIN_VALUE(child)
        node.alpha=child.value
        node.value=child.value
        #print "sodhi"
        printLine(node)
        return child

    points=numberOfChances(node.board,turn)
    #print len(points),"ariiiiiiiiiiiiiiiiiiiii"
    dummy_value=-9999
    for p in points:
        child=Node()
        tempBoard = copy.deepcopy(node.board)
        if turn =='X':
            modifyX(tempBoard,p.x,p.y)
        else: 
            modifyY(tempBoard,p.x,p.y)
        child.x=p.x
        child.y=p.y
        #print p.x,p.y,"lalalal"
        #printBoard(tempBoard)
        child.board=tempBoard
        child.depth=node.depth+1
        #print "in for loop ,max: 641"
        printLine(node)
        #print child.depth,child.value,child.alpha,child.beta,"this is to be delteted"
        #printLine(child)
        child.value = node.beta
        dummy_value=max(dummy_value,MIN_VALUE(child).value)
        #print "in for loop max, 644"
        #print dummy_value,"in max"
        node.alpha=dummy_value
        if node.alpha <= child.value:
            if child.depth == 1:
                node.nextX = child.x
                node.nextY = child.y
        node.value=dummy_value
        printLine(node)
        if dummy_value>=node.beta:
            return node
        if node.alpha < child.value:
            node.alpha = child.value
            if child.depth == 1:
                node.nextX = child.x
                node.nextY = child.y
    return node          
def MIN_VALUE(node):
    if node.depth>findepth:
        node.value=calcScore(node.board,turn1,8,8)
        return node
    #print len(numberOfChances(node.board, turn1)), "-----------------------"
    if len(numberOfChances(node.board,turn1))==0:
        #print "pass ",node.depth,node.value,node.alpha,node.beta
        #node.value = 9999
        printLine(node)
        #print "Min 0"
        #print "idiot"
        #print "i dont have moves in min,661"
        child=Node()
        child.flag=True
        child.depth=node.depth+1
        child.x=-2
        child.y=-2
        tempBoard = copy.deepcopy(node.board)
        child.board=tempBoard
        if node.flag==True:
            child.value=calcScore(child.board,turn1,8,8)
            child.x=-2
            child.y=-2
            printLine(child)
            #print "Min 1"
            node.value=child.value
            node.beta=child.beta
            printLine(node)
            #print "Min 2"
            return child
        #printLine(node)
        #print "in min, 675"
        child=MAX_VALUE(child)
        node.beta=child.value
        node.value=child.value
        #print "koottu"
        printLine(node)
        #print "Min 3"
        return child

    points=numberOfChances(node.board,turn1)
    #print len(points),"yedho oka sodhi"
    dummy_value=9999
    for p in points:
        child=Node()
        tempBoard = copy.deepcopy(node.board)
        if turn1 =='X':
            modifyX(tempBoard,p.x,p.y)
        else: 
            modifyY(tempBoard,p.x,p.y)
        child.x=p.x
        child.y=p.y
        #print child.x,child.y
        #pr(child.x,child.y)
        child.board=tempBoard
        #printBoard(child.board)
        child.depth=node.depth+1
        printLine(node)
        #printLine(child)
        dummy_value=min(dummy_value,MAX_VALUE(child).value)
        #print dummy_value,"in min"
        node.value=dummy_value
        node.beta=dummy_value
        printLine(node)
        if dummy_value<=node.alpha:
            return node
        node.beta=min(node.beta,node.value)
    return node

ALPHA_BETA(node)
