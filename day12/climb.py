from typing import List

class Vertex:
   
    def __init__(self, x: int, y: int, elevation: str) -> None:
        self.x = x
        self.y = y
        self.elevation = self.conv_elev(elevation)
        self.neigh = {}
        
        self.prev: int = None
    
    def get_id(self) -> int:
        return self.x + row_count * self.y
    
    def conv_elev(self, elev_str: str):
        if elev_str == 'S':
            return ord('a') - 97
        elif elev_str == 'E':
            return ord('z') - 97
        else:
            return ord(elev_str) - 97
        
    def add_edge(self, target):
        if target.elevation - self.elevation <= 1:
            self.neigh[str(target.get_id())] = 1

def add_edges(graph: List[Vertex], row_count: int):
    for v in graph:
        if v.get_id() - row_count >= 0:
            v.add_edge(graph[v.get_id() - row_count])
        if v.get_id() + row_count < len(graph):
            v.add_edge(graph[v.get_id() + row_count])
        if v.get_id() - 1 >= 0:
            v.add_edge(graph[v.get_id() - 1])
        if v.get_id() + 1 < len(graph):
            v.add_edge(graph[v.get_id() + 1])

def dijkstra(graph: List[Vertex], src: int, end: int) -> List[int]:
    dist = [1e7] * len(graph)
    dist[src] = 0
    q: List[int] = []
    pop_dist = [1e7] * len(graph)
    pop_dist[src] = 0
    u = -1
    for i in range(len(graph)):
        q.append(i)
        
    while len(q) > 0:
        u = pop_dist.index(min(pop_dist))
        if u == end or u not in q:
            break
        q.remove(u)
        pop_dist[u] = 1e7
        for n in graph[u].neigh.keys():
            if int(n) in q:
                alt = dist[u] + graph[u].neigh[n]
                if alt < dist[int(n)]:
                    dist[int(n)] = alt
                    pop_dist[int(n)] = alt
                    graph[int(n)].prev = u
    
    return dist

row_count: int = -1
start = -1
end = -1
graph: List[Vertex] = []

with open('day12/area.txt') as f:
    tmp = [x.strip() for x in f.readlines()]
    area = [[x[i] for i in range(len(x))] for x in tmp]
    row_count = len(area[0])
    for i in range(len(area)):
        line = []
        for j in range(len(area[i])):
            tmp = Vertex(j, i, area[i][j])
            line.append(tmp)
            if area[i][j] == 'S':
                start = tmp.get_id()
            elif area[i][j] == 'E':
                end = tmp.get_id()
        graph += line

add_edges(graph, row_count)
part1= dijkstra(graph, start, end)

print(part1[end])
part2 = []
for i in range(len(graph)):
    if graph[i].elevation == 0:
        part2.append(dijkstra(graph, i, end)[end])
print(min(part2))
