import numpy as np
np.set_printoptions(legacy='1.13')

if __name__ == '__main__':
    read = input().split(' ')
    N = int(read[0])
    M = int(read[1])

    print(np.eye(N, M))