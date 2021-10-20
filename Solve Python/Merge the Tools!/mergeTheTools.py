def merge_the_tools(string, k):
    # your code goes here
    result = [sorted(set(string[i:k+i]), key=string[i:k+i].index) for i in range(0,len(string),k)]

    for value in result:
        print("".join(x for x in value))
        
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)