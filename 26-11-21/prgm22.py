lst = []
n = int(input('enter the limit'))
for i in range(0, n):
    ele = int(input())
    lst.append(ele)
print(lst)
result = []
for i in lst:
    if i > 100:
        result.append('over')
    else:
        result.append(i)
print(result)