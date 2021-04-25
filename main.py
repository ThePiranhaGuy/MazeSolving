from astar import AstarNode
from dijkstra import Dnode
import cv2
import time

def main():
    maze = cv2.imread(r"normal.png")
    start = [4,8]  # starting position
    end = [81,94]  # ending position

    cost = 1  # cost per movement
    timestamp = time.time()
    res, counter = AstarNode.solve(maze, cost, start, end)
    timestamp = time.time()-timestamp
    print("==={} seconds===\n==={} steps===".format(timestamp, counter))
    if res is None:
        print("Nah. Check the Params correctly")
    else:
        cv2.imwrite('output.png', res)
        print("File output.png Written in root folder!")
    

if __name__ == '__main__':
    main()
