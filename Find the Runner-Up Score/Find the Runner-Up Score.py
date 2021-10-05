def result(n, arr):
    for i in range(0, n):
        value = arr[i]
        
        for j in range(i+1, n):
            if value > arr[j]:
                arr[i] = arr[j]
                arr[j] = value

    if arr[0] < -100 or arr[n-1] > 100:
        return

    biggest = arr[n-1]

    for i in range(1, n):
        if arr[n-i] < biggest:
            print(arr[n-i])
            return

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    
    if n < 2 or n > 10:
        exit(1)

    if (n != len(arr)):
        exit(1)

    result(n, arr)