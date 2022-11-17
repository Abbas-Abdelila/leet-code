class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        a_bottom = Point(ax1,ay1)
        a_top = Point(ax2, ay2)
        
        b_bottom = Point(bx1, by1)
        b_top = Point(bx2, by2)
        
        rec1_area = (a_bottom.x - a_top.x) * (a_bottom.y - a_top.y)
        rec2_area = (b_bottom.x - b_top.x) * (b_bottom.y - b_top.y)
        
        total_area = rec1_area + rec2_area
        
        def intersect(a_bottom, a_top, b_bottom, b_top):
            x1, y1 = max(a_bottom.x, b_bottom.x), max(a_bottom.y, b_bottom.y)
            x2, y2 = min(a_top.x, b_top.x), min(a_top.y, b_top.y)
            
            if x1 > x2 or y1 > y2:
                return False
            else:
                return (x2-x1) * (y2-y1)
        
        intersect = intersect(a_bottom, a_top, b_bottom, b_top)
        if intersect:
            total_area -= intersect
        
        return total_area