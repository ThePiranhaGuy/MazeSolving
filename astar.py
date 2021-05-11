import numpy as np
import math

class AstarNode:
    
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0


    def __eq__(self, other):
        return self.position == other.position

    def distance(self,node,hType):    #returns eucledian distance from calling object to specified node
        if hType==1:
            return math.sqrt((self.position[0] - node.position[0])**2 + (self.position[1] - node.position[1])**2)
        elif hType==2:
            return (abs(self.position[0]-node.position[0]) + abs(self.position[1]-node.position[1]))
        elif hType==3:
            return max(abs(self.position[0]-node.position[0]),abs(self.position[1]-node.position[1]))

    def solve(maze, cost, start, end, steps = 8,hType = 1):
        start_node = AstarNode(None, tuple(start))
        start_node.g = start_node.h = start_node.f = 0
        end_node = AstarNode(None, tuple(end))
        end_node.g = end_node.h = end_node.f = 0


        unvisited_list = []
    
        visited_list = []

    
        unvisited_list.append(start_node)

        outer_iterations = 0
        max_iterations = (len(maze) // 2) ** 4
        if steps == 8:
            move = [[-1, 0],  # go up
                    [-1,-1],
                    [0, -1],  # go left
                    [-1,+1],
                    [ 1, 0],  # go down
                    [ 1, 1],
                    [ 0, 1],  # go right
                    [ 1,-1]]
        elif steps == 4 :
            move = [[-1, 0],  # go up
                    [0, -1],  # go left
                    [ 1, 0],  # go down
                    [ 0, 1]]  # go right
        else:
            print("error!")
            return None

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
                print("Aborting task. Too many iterations")
                break

            unvisited_list.pop(current_index)
            visited_list.append(current_node)

            if current_node == end_node:
                print("Computation Complete!")
                break
            children = []

            for new_position in move:

                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                if (node_position[0] > (no_rows - 1) or
                    node_position[0] < 0 or
                    node_position[1] > (no_columns - 1) or
                        node_position[1] < 0):
                    continue

                if (maze[node_position[0]][node_position[1]] != [0,0,0]).all():
                    continue

                new_node = AstarNode(current_node, node_position)
                maze[node_position[0],node_position[1]] = [50,88,239]
                children.append(new_node)

            for child in children:

                if len([visited_child for visited_child in visited_list if visited_child == child]) > 0:
                    continue

                child.g = current_node.g + cost

                child.h = child.distance(end_node,hType)    #HERE 

                child.f = child.g + (child.h)

                # Child is already in the yet_to_visit list and f cost is already lower 
                if len([i for i in unvisited_list if child == i and child.f > i.f]) > 0:
                    continue

                unvisited_list.append(child)

        count=0
        # we update the path of start to end found by A-star search with every step incremented by 1
        while current_node is not None:
            count+=1
            maze[current_node.position[0],current_node.position[1]] = [239,88,50]
            current_node = current_node.parent
        return (maze, count)
