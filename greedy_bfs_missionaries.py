# GREEDY BEST-FIRST SEARCH
# RA32311003011472 DEV VIKNESH A D 
import heapq
class State:
    def __init__(self, missionaries, cannibals, boat, parent=None):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = parent
    
    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if (self.missionaries < self.cannibals and self.missionaries > 0) or (3 - self.missionaries < 3 - self.cannibals and 3 - self.missionaries > 0):
            return False
        return True
    
    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0
    
    def get_children(self):
        moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
        children = []
        direction = -1 if self.boat else 1
        
        for m, c in moves:
            new_state = State(self.missionaries + direction * m, self.cannibals + direction * c, self.boat + direction, self)
            if new_state.is_valid():
                children.append(new_state)
        
        return children
    
    def __repr__(self):
        return f"({self.missionaries}, {self.cannibals}, {self.boat})"
    
    def __lt__(self, other):
        return heuristic(self) < heuristic(other)

def heuristic(state):
    return state.missionaries + state.cannibals  # Simple heuristic

def greedy_bfs():
    initial_state = State(3, 3, 1)
    queue = [(heuristic(initial_state), initial_state)]
    heapq.heapify(queue)
    visited = set()
    
    while queue:
        _, current = heapq.heappop(queue)
        
        if current.is_goal():
            return get_solution_path(current)
        
        visited.add((current.missionaries, current.cannibals, current.boat))
        
        for child in current.get_children():
            if (child.missionaries, child.cannibals, child.boat) not in visited:
                heapq.heappush(queue, (heuristic(child), child))
                visited.add((child.missionaries, child.cannibals, child.boat))
    
    return None

def get_solution_path(state):
    path = []
    while state:
        path.append(state)
        state = state.parent
    return path[::-1]

def main():
    print("RA2311003011472 DEV VIKNESH A D")
    print("GREEDY BEST-FIRST SEARCH:")
    solution = greedy_bfs()
    if solution:
        for step in solution:
            print(step)
    else:
        print("No solution found.")

if __name__ == "__main__":
    main()
