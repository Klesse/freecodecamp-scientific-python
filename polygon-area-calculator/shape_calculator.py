import re


class Rectangle:

  def __init__(self, width, heigth):
    self.width = width
    self.height = heigth

  def __str__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_perimeter(self):
    return 2 * self.width + 2 * self.height

  def get_area(self):
    return self.width * self.height

  def get_diagonal(self):
    return ((self.width**2 + self.height**2)**.5)

  def get_picture(self):
    result = ''
    if (self.height > 50 or self.width > 50):
      return 'Too big for picture.'
    else:
      for i in range(self.height):
        for j in range(self.width):
          result += '*'
        result += '\n'
    return result

  def get_amount_inside(self, sq):
    rect_area = self.get_area()
    sq_area = sq.get_area()
    if (rect_area >= sq_area):
      return rect_area // sq_area
    return 0


class Square(Rectangle):

  def __init__(self, side):
    self.height = side
    self.width = side

  def __str__(self):
    return f"Square(side={self.width})"

  def set_side(self, side):
    self.height = side
    self.width = side

  def set_width(self, side):
    self.height = side
    self.width = side

  def set_height(self, side):
    self.height = side
    self.width = side
