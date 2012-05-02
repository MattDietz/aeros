class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Size(Point):
    """Helper class that really just represents a point"""
    
    def __init__(self, x, y):
        super(Size, self).__init__(x, y)
    
    @property
    def width(self):
        return self.x

    @property
    def height(self):
        return self.y


