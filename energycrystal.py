import math

def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        result = ((int(math.log(x, 2)) + 1) * 2 + 1)
        print(result)

if __name__ == "__main__":
    main()