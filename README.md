# Robot walks in mazes project
Hand-on instruction to solve Maze problem using both DFS and BFS

## Introduction
**Robots**:
* Two different types of robots:
  1. Robot without wheel(Legged Robot): can only walk step by step
  2. Robot with wheel(Self-driving Car, Wheeled Robot): can move until it is blocked

**Mazes**:
* Two different types of mazes:
  1. Clear Route (like Street, Highway)
  
     <img width="200" alt="image" src="https://github.com/RuichenCN/Robot-walks-in-maze-project/blob/main/maze_tree_level1.png">
  2. Unclear Route (like Hotel, Hospital)
  
     <img width="400" alt="image" src="https://github.com/RuichenCN/Robot-walks-in-maze-project/blob/main/maze_matrix.png">
     
     The traversal sequence is "Right ==> Left ==> Top ==> Bottom"

**Traversals**:
* Two different ways of traversals:
  1. Deep First Traversal - does not find the Shortest Path
  2. Bread First Traversal - find the Shortest Path

**Problem discription**:
* Use DFT and BFT to solve thses two problems separately:
  1. Robot without wheel walks in the clear route maze
  2. Robot with wheel rolls in the unclear route maze
## Deep First Traversal
#### [Robot without wheel walks in the clear route maze]()
<img width="200" alt="image" src="https://github.com/RuichenCN/Robot-walks-in-maze-project/blob/main/maze_tree_level1.png">
* First: Convert the graph into a tree
  <img width="800" alt="image" src="https://github.com/RuichenCN/Robot-walks-in-maze-project/blob/main/tree.png">
* Second: Use DFT to find the exist position of the maze
  > Tip: DFT uses Stack as data structure
  <img width="800" alt="image" src="https://github.com/RuichenCN/Robot-walks-in-maze-project/blob/main/stack.png">
  
  * Step 1: Initialize the stack.
  * Step 2: Mark S as visited and put it onto the stack. Explore any unvisited adjacent node from S. We have two nodes A and B. Let's follow alphabetical order and pick A.
  * Step 3: Mark A as visited and put it onto the stack. Here A does not have any unvisited adjacent node. So, we pop A from the stack.
  * Step 4: We check the stack top for return to the previous node and check if it has any unvisited nodes. Here, we find S to be on the top of the stack.
  * Step 5: Only unvisited adjacent node from S is B now. So we visit B, mark it as visited and put it onto the stack. Explore any unvisited adjacent node from B. We have two nodes C and D. Let's follow alphabetical order and pick C.
  
  * Step 6: Mark C as visited and put it onto the stack. Here C does not have any unvisited adjacent node. So, we pop C from the stack.
  
  * Step 7: We check the stack top for return to the previous node and check if it has any unvisited nodes. Here, we find B to be on the top of the stack.
  
  * Step 8: Only unvisited adjacent node from B is D now. So we visit D, mark it as visited and put it onto the stack. Explore any unvisited adjacent node from D. We have two nodes E and F. Let's follow alphabetical order and pick E.
  
  * Step 9: Mark E as visited and put it onto the stack. Here E does not have any unvisited adjacent node. So, we pop E from the stack.
  
  * Step 10: We check the stack top for return to the previous node and check if it has any unvisited nodes. Here, we find D to be on the top of the stack.
  
  * Step 11: Only unvisited adjacent node from D is F now. So we visit F, mark it as visited and put it onto the stack. Explore any unvisited adjacent node from F. We have two nodes G and H. Let's follow alphabetical order and pick G.
  
  * Step 12: Mark G as visited and put it onto the stack. Here G does not have any unvisited adjacent node. So, we pop G from the stack.
  
  * Step 13: We check the stack top for return to the previous node and check if it has any unvisited nodes. Here, we find F to be on the top of the stack.
  
  * Step 14: Only unvisited adjacent node from F is H now. So we visit H, mark it as visited and put it onto the stack. Explore any unvisited adjacent node from H. We have two nodes I and J. Let's follow alphabetical order and pick I.
  
  * Step 15: Mark I as visited and put it onto the stack. Here I does not have any unvisited adjacent node. So, we pop I from the stack.
  
  * Step 16: We check the stack top for return to the previous node and check if it has any unvisited nodes. Here, we find H to be on the top of the stack.
  
  * Step 17: Only unvisited adjacent node from H is J now. So we visit J, mark it as visited and put it onto the stack. So, the final result for the maze is S-B-D-F-H-J.

#### [Robot with wheel rolls in the clear route maze]()
<img width="400" alt="image" src="https://github.com/RuichenCN/Robot-walks-in-maze-project/blob/main/maze_matrix.png">
* Use DFT from 0 to 1 in the matrix
  <img width="800" alt="image" src="https://github.com/RuichenCN/Robot-walks-in-maze-project/blob/main/queue.png">
  
  * Step1: Initialize the stack and mark 0 as visited and put it onto the stack.
  * Step2: The search sequence is “Right ==> Left ==> Up ==> Down”. We can’t go to right. So, we go left. We mark C as visited and put it onto the stack.
  * Step3: We can’t go right or left or up. So we go down. We mark G as visited and put it onto the stack.
  * Step4: We can go right. We mark H as visited and put it onto the stack.
  * Step5: We can’t go right or left or up. So we go down. We mark K as visited and put it onto the stack.
  * Step6: There is no way to go. So, we pop K from the stack.
  * Step7: There is still no way to go. So, we pop H from the stack.
  * Step8: We can’t go right. So we go left. We mark F, E, D as visited and put them onto the stack.
  * Step9: We can’t go right or left. So we go up. We mark A as visited and put it onto the stack.
  * Step10: We can go right. We mark B as visited and put it onto the stack.
  * Step11: There is no way to go. So, we pop B from the stack.
  * Step12: There is no way to go. So, we pop A from the stack.
  * Step13: We can’t go right or left or up. So we go down. We mark I as visited and put it onto the stack.
  * Step14: We can go right. So, we mark J, 1 as visited and put them onto the stack. We reach the destination.
## Bread First Traversal
#### [Robot with wheel rolls in the clear route maze]()
<img width="400" alt="image" src="https://github.com/RuichenCN/Robot-walks-in-maze-project/blob/main/maze_matrix2.png">

> Tip: BFT uses Queue as data structure

* Detail steps:
  
  * Step1:  
      Visited: 0 
               0  
      Queue:
   
  * Step2:  
      Visited: 0 
               1  
      Queue: 0
      1. Add 0 to the queue
      2. Mark 0 as visited
  
  * Step3:  
      Visited: 0
               1  
      Queue: 
      1. Remove 0 from the queue
      2. Print 0
  
  * Step4:  
      Visited: 0 C K
               1 1 1  
      Queue: C K
      1. Add C and K to the queue
      2. Mark C and K as visited
  
  * Step5:  
      Visited: 0 C K
               1 1 1   
      Queue: K
      1. Remove C from the queue
      2. Print 0 C
  
  * Step6:  
      Visited: 0 C K G 
               1 1 1 1  
      Queue: K G
      1. Add G to the queue
      2. Mark G as visited
  
  * Step7:  
    Visited: 0 C K G
             1 1 1 1  
    Queue: G
    1. Remove K from the queue
    2. Print: 0 C K
  
  * Step8:  
    Visited: 0 C K G 
             1 1 1 1  
    Queue: 
    1. Remove G from the queue
    2. Print 0 C K G
  
  * Step9:  
    Visited: 0 C K G D
             1 1 1 1 1   
    Queue: D
    1. Add D to the queue
    2. Mark D as visited
  
  * Step10:  
    Visited: 0 C K G D
             1 1 1 1 1   
    Queue:
    1. Remove D from the queue
    2. Print: 0 C K G D
  
  * Step11:  
    Visited: 0 C K G D A I
             1 1 1 1 1 1 1   
    Queue: A I
    1. Add A, I to the queue
    2. Mark A, I as visited
  
  * Step12:  
    Visited: 0 C K G D A I
             1 1 1 1 1 1 1   
    Queue: I
    1. Remove A from the queue
    2. Print: 0 C K G D A
  
  * Step13:  
    Visited: 0 C K G D A I B
             1 1 1 1 1 1 1 1   
    Queue: I B
    1. Add B to the queue
    2. Mark B as visited
  
  * Step14:  
    Visited: 0 C K G D A I B
             1 1 1 1 1 1 1 1   
    Queue: B
    1. Remove I from the queue
    2. Print: 0 C K G D A I
  
  * Step15:  
    Visited: 0 C K G D A I B U
             1 1 1 1 1 1 1 1 1   
    Queue: B U
    1. Add U to the queue
    2. Mark U as visited
    Note: Because the ball doesn’t stop until reach a wall, the ball can’t get the destination R.
  
  * Step16:  
    Visited: 0 C K G D A I B U
             1 1 1 1 1 1 1 1 1   
    Queue: U
    1. Remove B from the queue
    2. Print 0 C K G D A I B
  
  * Step17:  
    Visited: 0 C K G D A I B U
             1 1 1 1 1 1 1 1 1   
    Queue: 
    1. Remove U from the queue
    2. Print 0 C K G D A I B U
  
  * Step18:  
    Visited: 0 C K G D A I B U P
             1 1 1 1 1 1 1 1 1 1   
    Queue: P
    1. Add P to the queue
    2. Mark P as visited
  
  * Step19:  
    Visited: 0 C K G D A I B U P
             1 1 1 1 1 1 1 1 1 1   
    Queue: 
    1. Remove P from the queue
    2. Print 0 C K G D A I B U P
  
  * Step20:  
    Visited: 0 C K G D A I B U P J M
             1 1 1 1 1 1 1 1 1 1 1 1   
    Queue: J M 
    1. Add J and M to the queue
    2. Mark J and M as visited
  
  * Step21:  
    Visited: 0 C K G D A I B U P J M
             1 1 1 1 1 1 1 1 1 1 1 1   
    Queue: M 
    1. Remove J from the queue
    2. Print 0 C K G D A I B U P J
  
  * Step22:  
    Visited: 0 C K G D A I B U P J M
             1 1 1 1 1 1 1 1 1 1 1 1   
    Queue: 
    1. Remove M from the queue
    2. Print 0 C K G D A I B U P J M
    End
## Related Leetcode question
LC 490 [The Maze](https://leetcode.com/problems/the-maze/)
* Solution code
  * [DFT](https://github.com/RuichenCN/Robot-walks-in-maze-project/blob/main/solution_DFT.py)
  * [BFT](https://github.com/RuichenCN/Robot-walks-in-maze-project/blob/main/solution_BFT.py)

## Reference
* Graph [Graph Explanation](https://www.geeksforgeeks.org/graph-data-structure-and-algorithms/?ref=gcse)
* Tree [Tree Explanation](https://www.geeksforgeeks.org/binary-tree-data-structure/?ref=gcse)
* Depth-First-Search      [DFS Explaination](https://brilliant.org/wiki/depth-first-search-dfs/#complexity-of-depth-first-search)
* Breadth-First-Search      [BFS Explaination](https://www.youtube.com/watch?v=xlVX7dXLS64)

♥️
