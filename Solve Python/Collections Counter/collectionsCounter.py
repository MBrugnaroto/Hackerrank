# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

if __name__ == '__main__':
    x = int(input())
    t = Counter([int(x) for x in input().split()])
    n = int(input())

    for i in range(n):
        shoes, value = map(int, input().split())
        if t[shoes] > 0:
            value_total += value
            t[shoes] -= 1

    print(value_total)