def calcarea(len, wid):
  return len * wid

def calcperim(len, wid):
  return len * 2 + wid * 2

def areaPerim(len, wid):
  area = calcarea(len, wid)
  perim = calcperim(len, wid)
  return area, perim

def main():
  length = int(input("enter length: "))
  width = int(input("enter width: "))
  a, p = areaPerim(length, width)
  print(f"Area: {a}\nPerimeter: {p}")

if __name__ == "__main__":
  main()