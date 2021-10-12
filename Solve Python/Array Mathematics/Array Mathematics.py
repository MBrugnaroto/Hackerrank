import numpy as np

class PrintList:
    def print_list(self, aname):
        firstitem = True
        if isinstance(aname, list):
            print('[', end='')
            for item in aname:
                if isinstance(item, list):
                    if firstitem:
                        firstitem = False
                    else:
                        print()
                    self.print_list(item)
                else:
                    print(' {} '.format(item), end='')
            print(']', end = '')
        else:
            print('Not a list')

import numpy as np

if __name__ == '__main__':
    read = input().split(' ')
    N = int(read[0])
    M = int(read[1])
    a = []
    b = []
    result = []

    for i in range(N):
        x = input().split(' ')
        linha = []

        for i in range(M):
            linha.append(int(i))

        a.append(x)

    for i in range(N):
        x = input().split(' ')
        linha = []

        for i in range(M):
            linha.append(int(i))

        b.append(x)

    for i in range(N):
        linha=[]
        soma = 0

        for j in range(M):
            soma = int(a[i][j]) + int(b[i][j])
            linha.append(soma)
        
        result.append(linha)
    
    p = PrintList()
    p.print_list(result)
    print('\t')
    result = []

    for i in range(N):
        linha=[]
        soma = 0

        for j in range(M):
            soma = int(a[i][j]) - int(b[i][j])
            linha.append(soma)
        
        result.append(linha)
    
    p = PrintList()
    p.print_list(result)
    print('\t')
    result = []

    for i in range(N):
        linha=[]
        soma = 0

        for j in range(M):
            soma = int(a[i][j]) * int(b[i][j])
            linha.append(soma)
        
        result.append(linha)
    
    p = PrintList()
    p.print_list(result)
    print('\t')
    result = []

    for i in range(N):
        linha=[]
        soma = 0

        for j in range(M):
            soma = int(a[i][j]) // int(b[i][j])
            linha.append(soma)
        
        result.append(linha)
    
    p = PrintList()
    p.print_list(result)
    print('\t')
    result = []

    for i in range(N):
        linha=[]
        soma = 0

        for j in range(M):
            soma = int(a[i][j]) % int(b[i][j])
            linha.append(soma)
        
        result.append(linha)
    
    p = PrintList()
    p.print_list(result)
    print('\t')
    result = []

    for i in range(N):
        linha=[]
        soma = 0

        for j in range(M):
            soma = int(a[i][j]) ** int(b[i][j])
            linha.append(soma)
        
        result.append(linha)
    
    p = PrintList()
    p.print_list(result)
    result = []