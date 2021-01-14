import math
import collections
Point2D = collections.namedtuple('Point2D', ['x', 'y'])
x, y = input().split()
p1 = Point2D(x=int(x), y=int(y))
x, y = input().split()
p2 = Point2D(x=int(x), y=int(y))
a = p1.x - p2.x
b = p1.y - p2.y
c = math.sqrt((a * a) + (b * b))
print(c)