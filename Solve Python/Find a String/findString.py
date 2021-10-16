def count_substring(string, sub_string):
    result = sum([1 for i in range(len(string)-len(sub_string)+1) if string[i:len(sub_string)+i] == sub_string])

    return result

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)