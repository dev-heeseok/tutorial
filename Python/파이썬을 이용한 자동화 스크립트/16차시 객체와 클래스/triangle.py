class Shape(object):

    def __init__(self, number_of_sides) -> None:
        self.number_of_sides = number_of_sides

class Triangle(Shape):
    
    def __init__(self, edge1, edge2, edge3) -> None:
        super().__init__(3)
        self.edge1 = edge1
        self.edeg2 = edge2
        self.edge3 = edge3

tri = Triangle('side1', 'side2', 'side3')
print('edge num: {0}'.format(tri.number_of_sides))
print('e1: {0}, e2: {1}, e3: {2}'.format(tri.edge1, tri.edeg2, tri.edge3))
