from calcfunctions import *
def dosomething():
  print("Hello World!")

def printnums():
  x = 0
  while x < 10:
    print("x:",x)
    x += 1

def main():
  dosomething()
  printnums()
  q, r = divmod2(5, 10)
  print(q, r)

if __name__ == "__main__":
  main()