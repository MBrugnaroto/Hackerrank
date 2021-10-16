def validateString(s):
    for validator in ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper']:
        print(any([True for i in s if eval('i.'+validator+'()')]))

if __name__ == '__main__':
    s = input()

    validateString(s)