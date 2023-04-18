from skimage.io import imread, imshow
from skimage import transform
import numpy as np
import matplotlib.pyplot as plt

original_image = imread("pic.jpg")
original_image = transform.resize(original_image,(512,512))

blocks = []

dup_img = np.copy(original_image)

dim = 512
jmp = 16

for x in range(0, dim, jmp):
    for y in range(0, dim, jmp):
        box = dup_img[x:x+jmp, y:y+jmp]
        blocks.append(box)

for x in range(0,16):
    for y in range(0,16):
        blocks[31][x][y] = [255,255,255]

goal_blocks = list(blocks)

np.random.shuffle(blocks)
init_blocks = list(blocks)

def displayImage(blocks):
    # Reassemble the shuffled blocks into a single image
    img = np.zeros_like(dup_img)
    idx = 0
    for i in range(0, 512, 16):
        for j in range(0, 512, 16):
            img[i:i+16, j:j+16] = blocks[idx]
            idx += 1

    return img

imshow(displayImage(goal_blocks))
plt.title("Goal Image")
plt.show()

imshow(displayImage(init_blocks))
plt.title("Init Image")
plt.show()

#Representing 16x16 boxes with a number to make comparison and computation easier
def findKey(arr):
    for key,value in encoded.items():
        if np.array_equal(value,arr):
            return key

b_id = 1
encoded = {}

for i in range(0,1024):

    if i == 31:
        encoded[0] = goal_blocks[i]
        continue

    encoded[b_id] = goal_blocks[i]
    b_id += 1

init = np.zeros((32, 32),dtype=int)
goal = np.zeros((32, 32),dtype=int)

iter = 0
for i in range(0,32):
    for j in range(0,32):

        arr = init_blocks[iter]
        id = findKey(arr)
        init[i][j] = id
        iter+=1

iter = 0
for i in range(0,32):
    for j in range(0,32):

        arr = goal_blocks[iter]
        id = findKey(arr)
        goal[i][j] = id
        iter+=1

def encoded2Image(arr):
    tempimg = np.zeros_like(dup_img)

    x = 0
    for i in range(0,32):
        y = 0
        for j in range(0,32):
            mapped_value = encoded[arr[i][j]]
            tempimg[x:x+16,y:y+16] = mapped_value
            y += 16
        x += 16
        

    imshow(tempimg)
    plt.show()#Forces the terminal to display image even of the code has not been fully executed

#Solving 8 Puzzle Problem
col = 32
check = 0

open_lis = [] #Piriority Queue
close_lis = []
moves = ["Up","Down","Left","Right"]

def costidx(n):  
    return n[1] 

def setPriority(lis): #Updates the whole Piriority Queue based on cost
    return sorted(lis,key=costidx)


def calCost(state): #Calculate Cost of the State
    return np.count_nonzero(np.not_equal(state, goal))


def findSpace(state):
    
    index = np.where(state == 0)
    row = index[0][0]
    col = index[1][0]

    return row,col

def generateStates(state,move):
    new_state = np.copy(state) 
    x,y = findSpace(state)  #Coordinates of empty space

    if move == "Up":
        if x != 0:      #Space not on top of the grid
            new_state[x][y],new_state[x-1][y] = new_state[x-1][y],new_state[x][y]
        
        return new_state

    elif move == "Down": 
        if x != col-1:      #Space not on the bottom of the grid
            new_state[x][y],new_state[x+1][y] = new_state[x+1][y],new_state[x][y]
        return new_state

    elif move == "Right":
        if y != col-1:    #Space not on rightmost position of the grid
            new_state[x][y],new_state[x][y+1] = new_state[x][y+1],new_state[x][y]  
        return new_state

    elif move == "Left":
        if y != 0:        #Space not on the leftmost position of the grid
            new_state[x][y],new_state[x][y-1] = new_state[x][y-1],new_state[x][y]  
        return new_state

def repeatedState(state):
    for arr,cost in open_lis:
        if np.array_equal(arr,state):
            return True

    for arr,cost in close_lis:
        if np.array_equal(arr,state):
            return True

    return False

def Astar():

    global open_lis
    global check

    if np.array_equal(init,goal):
        print(init,goal)
        return []

    init_cost = calCost(init)

    open_lis.append((init,init_cost))

    while len(open_lis)>0:
        arr,cost = open_lis.pop(0)

        if np.array_equal(arr,goal):
            close_lis.append((arr,cost))
            break

        for i in moves:
            newarr = generateStates(arr,i)

            if repeatedState(newarr):
                continue

            open_lis.append((newarr,calCost(newarr)))

        open_lis = setPriority(open_lis)
        close_lis.append((arr,cost))

    return close_lis[-1][0]

encoded2Image(Astar())

imshow(displayImage(init_blocks))
plt.title("Reconstructed Image")
plt.show()
