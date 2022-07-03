from numpy.lib.function_base import select
from astar import AstarNode
from dijkstra import Dnode
import numpy as np
import cv2
import time

def run(filename = r'input.png'):
    choice=-1
    
    maze = cv2.imread(filename)
    if maze is None:
        print('! Can\'t find image at{}'.format(filename))
        return -1
    start = [4,7]  # starting position
    end = [82,96]  # ending position
    print("choice:\n1:Dijkstra 2. Astar")
    choice = int(input())
    print('Steps: 4 / 8: ')
    steps = int(input())
    cost = 1  # cost per movement
    if choice == 1:
        timestamp = time.time()
        res, counter = Dnode.solve(maze, cost, start, end,steps=steps)
    if choice == 2:
        print("Enter Heuristic type: 2.1.Eucledian 2.2.Manhattan 2.3. Diagonal ")
        c = int(input())
        timestamp = time.time()
        res, counter = AstarNode.solve(maze, cost, start, end,steps = steps,hType=c)
    timestamp = time.time()-timestamp
    print("==={} seconds===\n==={} steps===".format(timestamp, counter))
    if res is None:
        print("Nah. Check the Params correctly")
    else:
        show = np.zeros((1000,1000,3),dtype=np.uint8)
        for i in range(1000):
            for j in range(1000):
                show[i,j] = res[i//10][j//10]
        cv2.namedWindow("output",cv2.WINDOW_NORMAL)
        cv2.imshow("output",show)
        cv2.waitKey(0)
        cv2.imwrite('output.png', res)
        print("File output.png Written in working folder!")
    
def main():
    print("Enter file path[-1 to use input.png]:")
    x = input()
    if(x=='-1'):
        run()
    else:
        run(x)



if __name__ == '__main__':
    main()
