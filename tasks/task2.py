# переменные для теста:
x_centr, y_center = 1, 1
radius = 5
points = [(0, 0), (1, 6), (6, 6)]

def points_coordinate(x_c, y_c, r, x, y):
    return (x - x_c)**2 / r**2 + (y - y_c)**2 / r**2

for x, y in points:
    print(points_coordinate(x_centr, y_center, radius, x, y))
