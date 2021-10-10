def secondeLowest(list_grade):
    list_grade.sort(key=lambda x:x[1])
    first_lowest = list_grade[0][1]

    while list_grade[0][1] == first_lowest:
        list_grade.pop(0)

    second_lowest = list_grade[0]
    
    result = [stundent for stundent in list_grade if stundent[1] == second_lowest[1]]
    result.sort(key=lambda x:x[0])

    for stundent in result: print(stundent[0])

if __name__ == '__main__':
    list_grade = []
    n = int(input())

    for _ in range(n):
        name = input()
        score = float(input())
        list_grade.append([name, score])

    if 2 <= n <=5:
        secondeLowest(list_grade)