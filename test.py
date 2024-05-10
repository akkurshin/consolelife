from time import sleep


class Map:
    def __init__(self):
        self.map = [
            [0,0,0,0,0],
            [0,1,1,1,0],
            [0,1,0,0,0],
            [0,1,0,1,0],
            [0,0,0,0,0],
        ]
        self.next_generation =  [
            [0,0,0,0,0],
            [0,1,1,1,0],
            [0,1,0,0,0],
            [0,1,0,1,0],
            [0,0,0,0,0],
        ]

    def print_map(self):
        for row in self.map:
            print(row)

    def get_neighbors(self, x, y):
        neighbors = []
        offsets = [[-1, 1], [0, 1], [1, 1],
                   [-1, 0],         [1, 0],
                   [-1,-1], [0,-1], [1,-1]]
        for offset in offsets:
            try:
                neighbors.append(self.map[x + offset[0]][y + offset[1]])
            except IndexError:
                continue
        return neighbors

    def count_alive_neighbors(self, neighbors: list) -> int: 
        live_count = 0
        for neighbor in neighbors:
            if neighbor == 1:
                live_count += 1
        return live_count
    
    def compute_next_generation(self):
        for x in range(len(self.map)):
            for y in range(len(self.map[x])):
                neighbors = self.get_neighbors(x,y)
                live_neighbors = self.count_alive_neighbors(neighbors)
                if self.map[x][y] == 0:
                    if live_neighbors == 3:
                        self.next_generation[x][y] = 1
                    else:
                        self.next_generation[x][y] = 0
                if self.map[x][y] == 1:
                    if live_neighbors == 2 or live_neighbors == 3:
                        self.next_generation[x][y] = 1
                    else:
                        self.next_generation[x][y] = 0
        self.map = self.next_generation

map = Map()

while True:
    map.print_map()
    print('_______________')
    map.compute_next_generation()
    sleep(2)

    