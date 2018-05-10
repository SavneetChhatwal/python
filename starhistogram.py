array = []
listlen = int(input())

for i in range(listlen):
    x = input()
    array.append(x)

for i in range(listlen):
    c = int(array[i])
    print('*'*c)
