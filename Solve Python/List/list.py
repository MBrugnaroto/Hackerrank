if __name__ == '__main__':
    N = int(input())
    arr = []

    for _ in range(N):

        s = input().rstrip().split(" ")
        cmd = s[0]
        args = s[1:]

        if cmd != "print":
            cmd += "("+ ",".join(args) +")"
            eval("arr."+cmd)
        else:
            print(arr)


"""
# Forma manual:

def machine(command, arr):
    command = command.split(' ')

    if command[0] == 'insert':
        arr[int(command[1]):int(command[1])] = [int(command[2])]
        return
    
    if command[0] == 'append':
        arr.append(int(command[1]))
        return

    if command[0] == 'sort':
        arr.sort()
        return
    
    if command[0] == 'pop':
        arr.pop()
        return

    if command[0] == 'reverse':
        arr[:] = arr[::-1]
        return

    if command[0] == 'remove':
        position = arr.index(int(command[1]))
        arr.pop(position)

    if command[0] == 'print':
        print(arr)
        return

if __name__ == '__main__':
    N = int(input())
    arr = []

    for i in range(N):
        command = str(input())
        machine(command, arr)
"""