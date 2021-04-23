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

    def eucledian_distance(self,node):    #returns eucledian distance from calling object to specified node
        return math.sqrt((self.position[0] - node.position[0])**2 + (self.position[1] - node.position[1])**2)
    def diagonal_distance(self,node):
        return max(abs(self.position[0]-node.position[0]),abs(self.position[1]-node.position[1]))
    def manhattan_distance(self,node):
        return (abs(self.position[0]-node.position[0]) + abs(self.position[1]-node.position[1]))

# This function return the path of the search
    def return_path(self, maze,visited):
        path = []               #adjecacy list for the path
        result  = maze.copy()
        current = self
        while current is not None:
            path.append(current.position)
            current = current.parent
        count = 1
        for i in visited:
            result[i.position[0],i.position[1]] = [50,88,239]
        # we update the path of start to end found by A-star search with every step incremented by 1
        for i in range(len(path)):
            result[path[i][0]][path[i][1]] = [239,88,50]
            count += 1
        return (result, count)


    def solve(maze, cost, start, end) -> np.ndarray:

        start_node = AstarNode(None, tuple(start))
        start_node.g = start_node.h = start_node.f = 0
        end_node = AstarNode(None, tuple(end))
        end_node.g = end_node.h = end_node.f = 0


        unvisited_list = []
    
        visited_list = []

    
        unvisited_list.append(start_node)

        outer_iterations = 0
        max_iterations = (len(maze) // 2) ** 10


        move = [[-1, 0],  # go up
#                [-1,-1],
                [0, -1],  # go left
#                [-1,+1],
                [ 1, 0],  # go down
#                [ 1, 1],
                [ 0, 1]]  # go right
#                [ 1,-1]]

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
                return current_node.return_path(maze,visited_list)

            unvisited_list.pop(current_index)
            visited_list.append(current_node)

            if current_node == end_node:
                print("Computation Complete!")
                return current_node.return_path(maze,visited_list)
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

                new_node = AstarNode(current_node, node_position)

                children.append(new_node)

            for child in children:

                if len([visited_child for visited_child in visited_list if visited_child == child]) > 0:
                    continue

                child.g = current_node.g + cost

                child.h = child.diagonal_distance(end_node)

                child.f = child.g + 10*(child.h + current_node.h)

                # Child is already in the yet_to_visit list and f cost is already lower 
                if len([i for i in unvisited_list if child == i and child.g > i.g]) > 0:
                    continue

                unvisited_list.append(child)

