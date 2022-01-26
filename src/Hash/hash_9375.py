# 9375 hash
from collections import Counter
test_case = int(input())

'''
# type_name이 있으면 뒤에 append. 없으면 추가
for i in range(test_case):
    num = int(input())
    answer = {}
    result = 1
    for j in range(num):
        name, type_name = input().split()
        
        if type_name not in answer.keys():
            answer[type_name] = [name]
        else:
            answer[type_name].append(name)
    for key in answer.keys():
        result = result * (len(answer[key])+1)
    print(result-1)
'''
for i in range(test_case):
    num = int(input())
    answer = []
    result = 1
    for j in range(num):
        name, type_name = input().split()
        answer.append(type_name)
    dic = Counter(answer)
    for key in dic.keys():
        result = result * (dic[key] + 1)
    print(result-1)
