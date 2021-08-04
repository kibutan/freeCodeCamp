class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height
  def __str__(self):
    return "Rectangle(width="+str(self.width)+", height="+str(self.height)+")"
  def set_width(self,w):
    self.width = w
  def set_height(self,h):
    self.height = h

  def get_area(self):
    return self.width * self.height
  def get_perimeter(self):
    return self.width * 2 +  self.height * 2
  def get_diagonal(self):
    return (self.width ** 2 + self.height**2)**.5
  def get_picture(self):
    if max(self.width,self.height) > 50:return "Too big for picture."
    else:
      body = "*"*self.width + "\n"
      body *= self.height
      body.rstrip()
      print(body)
      return body
  def get_amount_inside(self,shape):
    amount = self.get_area()//shape.get_area()
    return amount


class Square(Rectangle):
    def __init__(self,side):
      self.width = side
      self.height = side
    def __str__(self):
      return "Square(side="+str(self.width)+")"
    def set_side(self,side):
      self.width = side
      self.height = side
    
