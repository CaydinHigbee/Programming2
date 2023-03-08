class Shape:
  # Constructer: set up class data
  def __init__(self, length, width):
    self.length = length
    self.width = width
    self._area = 0
    self._perim = 0

  # Mutator/Setter: modifies class data
  def calculate(self):
    self.area = self.length * self.width
    self.perim = 2 * self.length + 2 * self.width

  
  def getArea(self):
    return self.area

  def getPerimeter(self):
    return self.perim


def main():
  len = int(input("Enter length: "))
  wid = int(input("Enter width: "))
  shape = Shape(len, wid) # Call "Shape" constructor
  shape.calculate()
  print("Area:", shape.getArea())
  print("Perimeter:", shape.getPerimeter())


if __name__ == "__main__":
  main()