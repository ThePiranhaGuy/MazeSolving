import numpy as np
import math

class Dnode:
    def __init__(self,parent = None, position = None):
        self.parent = parent
        self.position = position
        self.f=0 #cost

    def __eq__(self,other):
        return self.position == other.position


    def solve(maze,cost,start,end) ->np.ndarray:

        start_node = Dnode(None,tuple(start))
        start_node.f=0
        end_node = Dnode(None,tuple(end))
        end_node.f = 0
        

        unvisited_list = []
        visited_list = []
    
        unvisited_list.append(start_node)

        outer_iterations = 0
        max_iterations = (len(maze) // 2) ** 4

        move = [[-1, 0],  # go up
                [-1,-1],
                [0, -1],  # go left
                [-1,+1],
                [ 1, 0],  # go down
                [ 1, 1],
                [ 0, 1],  # go right
                [ 1,-1]]
        

        no_rows, no_columns,_ = maze.shape

        while len(unvisited_list) > 0:

            outer_iterations += 1

            current_node = unvisited_list[0]
            current_index = 0
            for index, item in enumerate(unvisited_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # if we hit this point return the path such as it may be no solution or
            # computation cost is too high
            if outer_iterations > max_iterations:
                print("giving up on pathfinding too many iterations")
                break

            unvisited_list.pop(current_index)
            visited_list.append(current_node)

            if current_node == end_node:
                print("Computation Complete!")
                break
            children = []

            for new_position in move:

                node_position = (
                    current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                if (node_position[0] > (no_rows - 1) or
                    node_position[0] < 0 or
                    node_position[1] > (no_columns - 1) or
                        node_position[1] < 0):
                    continue

                if (maze[node_position[0]][node_position[1]] != [0,0,0]).all():
                    continue

                new_node = Dnode(current_node, node_position)
                maze[node_position[0]][node_position[1]] = [50,88,239]
                children.append(new_node)

            for child in children:

                if child in visited_list:
                    continue

                child.f = current_node.f + cost

                if child in unvisited_list:
                    continue

                unvisited_list.append(child)
        
                count=0
        # we update the path of start to end found by Dijkstra search with every step incremented by 1
        while current_node is not None:
            count+=1
            maze[current_node.position[0],current_node.position[1]] = [239,88,50]
            current_node = current_node.parent
        return (maze, count)


