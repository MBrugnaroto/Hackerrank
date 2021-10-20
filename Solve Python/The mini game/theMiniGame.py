def minion_game(string):
    # your code goes here
    vowels = 'AEIOU'
    
    stuarsc = 0
    kevinsc = 0
    string = list(string)
    
    for i in range(len(string)):
        if string[i] in vowels:
            kevinsc += len(string) - i
        else:
            stuarsc += len(string) - i
    
    if stuarsc > kevinsc:
        print("Stuart %s"%stuarsc)
    
    elif stuarsc < kevinsc:
        print("Kevin %s"%kevinsc)
    
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)