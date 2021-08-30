# P45
# definition TowerOfHanoi function
def hanoi_c(n):
  if n == 0:
    return 0

  return 2 * hanoi_c(n - 1) + 1
 
def main():
  n = int(input())
  print("Number of moves:", hanoi_c(n))

if __name__ == "__main__":
    main()