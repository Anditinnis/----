from random import randint
import os

n = int(input())
a1 = int(input())
a2 = int(input())
sum_ = 0
item = 0
list = [randint(a1, a2) for i in range(n)]

for x in range(n):
    sum_ += int(x)
    item += 1

s = sum_/item
f = int(input())

with open('file1.txt', 'w+') as file:
    file.write(str(list) + '\n')

with open('file2.txt', 'w+') as file:
    file.write(str(list) + '\n')
   


if f == 1:
    with open('file1.txt', 'a+') as file:
        file.write(str(s))
        os.startfile('file1.txt')

elif f == 2:
     with open('file2.txt', 'a+') as file:
        file.write(str(s))
        os.startfile('file2.txt')


