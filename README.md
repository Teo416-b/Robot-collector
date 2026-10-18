Robot Collector 

Description:
A Python program that simulates the movement of a 'robot' in a 2d world with obstacles and objects. 

Details:
-The robot can move using two different strategies (BFS and Sweep)
- The Robot has a limit of 80 steps. 
- The world is loaded from text files ('World 1.txt', 'World 2.txt', etc.). 
- You can customize each world to your liking, by using the symbols correctly 
- Symbols in the world: 
	• . -> Empty 
	• * -> Star/coin 
	• # -> Obstacle  


How to run:

-Choose a world by typing 1, 2, 3, or 4. Then the world they selected is displayed.
-Choose a strategy by typing 1-2:
	1. BFS (Breadth-First Search): Finds the shortest path to each coin.
	2. Sweep (like a typewriter): Scans the world line by line.

- The robot stops when:
	• It collects all available star, or
	• It reaches the 80-step limit.

- The robot's stats that appear after exploration:
	• The items it collected or didn’t collect
	• The path it followed for each star (if the user chose BFS)
	• The total steps it took

- The world is shown without the stars the robot has collected
- The program tells the user if the exploration ended because all stars were collected or because the robot reached 80 steps