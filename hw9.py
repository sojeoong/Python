#연습문제 11.3 hw9.py
class Point:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

    def show(self):
        return (f'({self.x},{self.y})')

    def set(self,x,y):
        self.x=x
        self.y=y

    def get(self):
        t=(self.x,self.y)
        return t

class Rectangle:
    def __init__(self,x1,y1,x2,y2):
        self.lt=Point(x1,y1)
        self.rb=Point(x2,y2)
    def show(self):
        print(f'좌측 상단 꼭지점이 {self.lt.show()}이고 우측 상단 꼭지점이 {self.rb.show()}인 사각형입니다.')
    def getWidth(self):
        return (self.rb.x-self.lt.x)
    def getHeight(self):
        return (self.rb.y-self.lt.y)
    def getArea(self):
        return Rectangle.getWidth(self)*Rectangle.getHeight(self)
    def getPerimeter(self):
        return (Rectangle.getWidth(self))*2+(Rectangle.getHeight(self))*2

# 주 프로그램부


r1 = Rectangle(5, 5, 20, 10)
a = r1.getArea()
p = r1.getPerimeter()
r1.show()
print(f'\n넓이는 {a}, 둘레는 {p}')