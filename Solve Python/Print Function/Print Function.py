if __name__ == '__main__':
    n = int(input())

    if n >= 1 and n <= 150:
        string = ""

        for i in range(1, n+1):
            string = string + str(i)

        print(string)