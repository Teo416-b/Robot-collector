from collections import deque

def bfs(cordList, start, goal):         #Creation of BFS

    rows, cols = len(cordList), len(cordList[0])        #defining the borders of the map
    queue = deque([start])                              #Making a two-way list
    visited = {start: None}                             #list to save the spots the robot has visited
    while queue:                        #loop for finding the shortest path to the star
        x, y = queue.popleft()
        if (x, y) == goal:
            steps = 0                   #step counter for the path
            path = []                   #list to save the path
            while (x ,y) is not None:
                    path.append((x, y))
                    steps += 1
                    if visited[(x, y)] is None:
                        break

                    (x, y) = visited[(x, y)]

            return path[::-1], steps-1


        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:               #all the directions the robot can move
            nx = x+dx
            ny = y+dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if cordList[nx][ny] != "#" and (nx, ny) not in visited:
                    visited[(nx, ny)] = (x, y)
                    queue.append((nx, ny))
    
    return None, 0

def main():         #creation of main

    print("")
    World = "nothing.txt"
    flag = 1
    while flag == 1:
        print("-----------LOAD WORLD-----------")               #menu to load worlds
        print("Choose World(1, 2, 3, 4)")
        print("--------------------------------")
        try:
            Chosen = int(input("Type only the number of the world: "))      #selecting the world the user chose
            if Chosen == 1:
                World = "World 1.txt"
            
            elif Chosen == 2:
                World = "World 2.txt"
            
            elif Chosen == 3:
                World = "World 3.txt"
            
            elif Chosen == 4:
                World = "World 4.txt"
                
            with open(World, "r", encoding="utf-8") as f:       #transferring the map form the txt to a 2d list
                cordList = []
                for w in f:
                    temp = list(w.strip().split())   
                    cordList.append(temp)
            flag = 0
        except ValueError:                                      #Printing erros in case the user gives an incorrect input
            print("\n")
            print("///////////////////////////////////////")
            print("Type only the number. E.g 1. Try again.")
            print("///////////////////////////////////////\n\n")
            flag = 1
        except FileNotFoundError:
            print("\n")
            print("//////////////////////////////////")
            print("World", Chosen, "doesn't exist. Try again.")
            print("//////////////////////////////////\n\n")
            flag = 1

    
    print("\n")                     
    print("____________________")                   #printing the map for the user to see it
    for c in cordList:
            print(" ".join(c))
    print("____________________")

    stars = []
    totalstars = 0
    for i in range(len(cordList)):                  #making a list containing all the statrs and their coordinates
        for j in range(len(cordList[i])):
            if cordList[i][j] == "*":
                stars.append((i, j))
                totalstars += 1
          
    print("Stars (*) = coins, dots (.) = empty space, hashtag (#) = obstacle\n")
    print("--------------------STRATEGY--------------------")               #menu for the user to chose a strategy fro the robot to explore the map
    print("Select strategy to traverse the world.")
    print("1. BFS (Breadth-First Search)")
    print("2. Sweep(Like a typewriter)")
    print("------------------------------------------------")

    flag2 = 1
    selection = 0
    while flag2 == 1:
        try:
            selection = int(input("Type 1 or 2 only: "))
            if selection == 1 or selection == 2:
                flag2 = 0
                print("")
            else:                               
                print("")
                print("////////////////////////////////////////////////////")                   #Printing erros in case the user gives an incorrect input
                print("incorrect input, only 1 or 2 are accepted. Try again.")
                print("////////////////////////////////////////////////////\n")
                
        except ValueError:
            print("")
            print("////////////////////////////////////////////////////")
            print("incorrect input, only 1 or 2 are accepted. Try again.")
            print("////////////////////////////////////////////////////\n")
            flag2 = 1

    print("\n")
    coins = 0                    #using Bfs to exlpore the map
    totalSteps = 0
    flag3 = 0
    remove = []                  #list for the stars collected
    if selection == 1:
        start = (0, 0)
        for star in stars:
            path, steps = bfs(cordList, start, star)
            totalSteps += steps                         #counter for the total number of steps taken 
            if totalSteps <= 80:                        #if the steps reach 80 the journey ends
                if path:
                    print("---------------------------------------------------------------------------------------")            #each time a object is collected its coordinates and the path used is shown
                    print(f"The star with coordinates {star} has been collected. The path taken is: {path}. \nThe number of steps is: {steps}")
                    print("---------------------------------------------------------------------------------------\n")
                    coins += 1
                    remove.append((star))
                    start = star                    #the robot continues to explore form the last object collected
            
            else:
                flag3 = 1                           #flag to print the msg that the journey ended because the robot reached 80 steps
                break


        for star in stars:
            path = bfs(cordList, start, star)
            if star not in remove:
                print("----------------------------------------------------")           #printing the objects colleccted 
                print(f"The star with coordinates {star}, wasn't collected")
                print("----------------------------------------------------\n")
  
    else:                                   #using sweep to explore the map
        totalSteps = 0
        coins = 0
        flag3 = 0
        flag4 = 0
        remove = []
        for i in range(len(cordList)):          
            if totalSteps < 80:                         #if the steps reach 80 the journey ends
                for j in range(len(cordList[i])):
                    if cordList[i][j] != "#":           #if the robot finds an obstacle it goes to the next line 
                        totalSteps += 1
                        if totalSteps == 80:
                            flag3 = 1                   #flag to print the msg that the journey ended because the robot reached 80 steps
                            break
                        if cordList[i][j] == "*":       #checking if the spot the robot is has an object
                            coins += 1
                            remove.append((i, j))
                            if totalstars == coins:     #if all the coins are collected the journey ends
                                flag4 = 1
                                break
                    else:
                        break
            else:
                break
            if flag4 == 1:
                break

        for r in remove:
            print("------------------------------------------------------")         #after the journey the stars collected and their coordinates are shown
            print(f"The star with coordinates", r,"has been collected.")
            print("------------------------------------------------------\n")
        for star in stars:
                if star not in remove:
                    print("----------------------------------------------------")           #after the journey the stars not collected are shown
                    print(f"The star with coordinates", star,"wasn't collected")
                    print("----------------------------------------------------\n")

    print("\n--------------STATS--------------")            #showing the stats of the robot
    print("Coins collected:",coins)
    if flag3 == 1:
        print("Steps taken: 80")
    else:
        print("Steps taken:", totalSteps )

    for (x , y) in remove:
        cordList[x][y] = '.'

    print("\nThe map after the journey of the robot")       #showing the map without the objects collected
    print("____________________")

    for c in cordList:
        print(" ".join(c))

    print("____________________")

    if flag3 == 1 :                                                     #showing why the journey ended
        print("The journey ended because the robot reached 80 steps\n")
    else:
        print("The journey ended because the robot collected all accessable coins\n")


main()

    