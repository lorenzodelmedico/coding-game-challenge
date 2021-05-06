import sys
import math
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


# stratégie à atteindre : tant que tt les arbres ne sont pas grade 2, on les montes puis tant que 3 des arbres ne sont pas grade 3 on les monte puis on convertit autant que possible ! 
#problème actuel : mauvaise gestion de la croissance des arbres (les compteurs/bool font mal le travail)


# strategy to be achieved: as long as all the trees are not grade 2, we mount them then as long as 3 of the trees are not grade 3 we mount them then we convert as much as possible!
# current problem: poor management of tree growth (counters / bool do the job badly)

number_of_cells = int(input())  # 37
for i in range(number_of_cells):
    # index: 0 is the center cell, the next cells spiral outwards
    # richness: 0 if the cell is unusable, 1-3 for usable cells
    # neigh_0: the index of the neighbouring cell for each direction
    index, richness, neigh_0, neigh_1, neigh_2, neigh_3, neigh_4, neigh_5 = [int(j) for j in input().split()]

# game loop
while True:
    myAction=""

    myCompleteAction=""
    myBestCompleteAction=""
    myMiddleCompleteAction=""

    littleChecker=False
    littleCellList=[]
    littleCount=4

    middleChecker=False
    middleCellList=[]
    middleCount=3

    collectTimer=False

    day = int(input())  # the game lasts 24 days: 0-23
    nutrients = int(input())  # the base score you gain from the next COMPLETE action
    # sun: your sun points
    # score: your current score
    sun, score = [int(i) for i in input().split()]
    inputs = input().split()
    opp_sun = int(inputs[0])  # opponent's sun points
    opp_score = int(inputs[1])  # opponent's score
    opp_is_waiting = inputs[2] != "0"  # whether your opponent is asleep until the next day
    number_of_trees = int(input())  # the current amount of trees

    for i in range(number_of_trees):
        inputs = input().split()
        cell_index = int(inputs[0])  # location of this tree
        size = int(inputs[1])  # size of this tree: 0-3
        is_mine = inputs[2] != "0"  # 1 if this is your tree
        is_dormant = inputs[3] != "0"  # 1 if this tree is dormant
        if (is_mine) and not is_dormant and size<2:
            littleCount-=1
            littleCellList.append(cell_index)
        elif is_mine and not is_dormant and size<3:
            middleCount-=1
            middleCellList.append(cell_index)
        elif is_mine and not is_dormant and size==3:
            collectTimer=True

    number_of_possible_actions = int(input())  # all legal actions
    if littleCount==0:
        littleChecker=True
        littleCount=4
    if middleCount==0:
        middleChecker=True
        middleCount=3   

    for i in range(number_of_possible_actions):
        possible_action = input()  # try printing something from here to start with
        if not littleChecker:
            print(littleCellList, file=sys.stderr, flush=True)
            checkValue=""
            for x in littleCellList:
                checkValue+=str(x)
            if "GROW" in possible_action and checkValue in possible_action:
                myGrowthAction=possible_action
            continue

        if not middleChecker:
            print(middleCellList, file=sys.stderr, flush=True)
            checkValue=""
            for x in middleCellList:
                checkValue+=str(x)
            if "GROW" in possible_action and checkValue in possible_action:
                myGrowthAction=possible_action
            continue
                
        elif "COMPLETE" in possible_action and collectTimer:
            bestRange=range(1,7)
            middleRange=range(7,19)
            myCompleteAction=possible_action
            if [int(s) for s in possible_action.split() if s.isdigit()][-1] in bestRange:
                myBestCompleteAction=possible_action
            elif [int(s) for s in possible_action.split() if s.isdigit()][-1] in middleRange:
                myMiddleCompleteAction=possible_action
       
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    # # GROW cellIdx | SEED sourceIdx targetIdx | COMPLETE cellIdx | WAIT <message>
    # def switch_action(action):
    #     switcher = {
    #         1: "COMPLETE",
    #         2: "GROW",
    #     }
    #     return switcher.get(action, "WAIT")

    # bestRange=range(1,7)
    # middleRange=range(7,19)
    # myGrowthAction=possible_action
    # if [int(s) for s in possible_action.split() if s.isdigit()][-1] in bestRange:
    #     myBestGrowthAction=possible_action
    # elif [int(s) for s in possible_action.split() if s.isdigit()][-1] in middleRange:
    #     myMiddleGrowthAction=possible_action


    if myMiddleCompleteAction!="":
        myCompleteAction=myMiddleCompleteAction
    if myBestCompleteAction!="":
        myCompleteAction=myBestCompleteAction

    if myCompleteAction!="":
        myAction=myCompleteAction
    elif myGrowthAction!="":
        myAction=myGrowthAction
    else:
        myAction="WAIT"

    print(myAction)
   