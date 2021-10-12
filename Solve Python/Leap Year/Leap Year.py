def is_leap(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return True
            else:
                return False
        else:
            return True   
    else:
        return False

if __name__ == '__main__':
    year = int(input())

    if year >= 1900 and year <= 100000:
        print(is_leap(year))
    else:
        print(False)