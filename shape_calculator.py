class Rectangle:
    width = int()
    height = int()

    def __init__(self, width=int(), height=int()):
        self.width = width
        self.height = height

    def __repr__(self) -> str:
        return "Rectangle()"

    def __str__(self) -> str:
        a = "Rectangle(width={}, height={})".format(self.width, self.height)
        return a

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (2*self.width) + (2*self.height)

    def get_diagonal(self):
        return (((self.width ** 2) + (self.height ** 2)) ** 0.5)

    def get_picture(self):
        picture = str()
        if self.width < 50 and self.height < 50:
            for i in range(self.height):
                for j in range(self.width):
                    picture += '*'
                # if self.height-1 > i:
                picture += '\n'
            return picture
        return "Too big for picture."

    def get_amount_inside(self, shape):
        # fit = int()
        # width = self.width
        # height = self.height-self.width
        # if width >= shape.width and height >= shape.height:
        #     while height >= shape.height:
        #         print('while {} >= {}'.format(height, shape.height))
        #         while width >= shape.width:
        #             print('while {} >= {}'.format(width, shape.width))
        #             if width >= shape.width:
        #                 print('fit +1 dari width')
        #                 fit += 1
        #             width -= shape.width
        #         if height >= shape.height:
        #             print('fit +1 dari height')
        #             fit += 1
        #         height -= shape.height
        fit = int()
        large = Rectangle.get_area(self)
        large_shape = shape.get_area()
        while large >= large_shape:
            fit += 1
            large -= large_shape
        return fit


class Square(Rectangle):

    def __init__(self, width=int()):
        self.width = width
        self.height = width
    
    def __repr__(self) -> str:
        return "Square()"
    
    def __str__(self) -> str:
        a = "Square(side={})".format(self.width)
        return a

    def set_side(self, side):
        self.width = side
        self.height = side
