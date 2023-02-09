pi = 3.14159
radius = int(input("Enter the Radius: "))
def circArea():
  return float(pi) * radius**2

def circCirc():
  return 2 * float(pi) * radius

def main():
  circArea()
  circCirc()

if __name__ == "__main__":
  main()