class CountSquares:

    def __init__(self):
        self.ptsCount = defaultdict(int)
        self.pts = []

    def add(self, point: List[int]) -> None:
       self.ptsCount[tuple(point)] += 1
       self.pts.append(point)
         
    def count(self, point: List[int]) -> int:
        count = 0
        x,y = point

        for point in self.pts:
            px = point[0]
            py = point[1]
            if abs(px-x) != abs(py-y) or x == px or y == py:
                continue
            count += self.ptsCount[(x,py)] * self.ptsCount[(px,y)]
        return count



        
