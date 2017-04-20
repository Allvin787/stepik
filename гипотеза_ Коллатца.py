# stepik
Напишите функцию, которая для заданного натурального числа n генерирует последовательность чисел, описанную в гипотезе Коллатца:

Если n четное, то делим его пополам, если нечётное, то умножаем на 3 и прибавляем 1. С итогом вычисления снова проделываем эту операцию до тех пор, пока в результате не будет получено число 1.

Например, для числа n = 17 последовательность вычислений выглядит следующим образом:
17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1

Предполагается, что подобная последовательность остановится на числе 1 для любого начального натурального числа n. 

Формат ввода:
Строка, содержащая единственное целое число nn, n>0n>0.

Формат вывода:
Строка, содержащая последовательность целых чисел, разделённых пробелом.

Sample Input 1:
17
Sample Output 1:
17 52 26 13 40 20 10 5 16 8 4 2 1
Sample Input 2:
1
Sample Output 2:
1
#####################################################################
n = int(input())
print(n, end=' ')
while n > 1:
    if n % 2 == 0:
        a = n // 2
        n = a
        #print(n, end=' ')
    else:
        n = 3*n + 1
    print(n, end=' ')

#################


n = int(input())
print(n, end = ' ')
while n != 1:
    n = n//2 if n%2 == 0 else n*3+1
    print(n, end = ' ')
    
 ############################   

def collatzRecur(curNum):
    print(curNum, end = " ")
    if curNum<=1:
        return 0
    if curNum%2==0:
        return collatzRecur(curNum//2)
    else:
        return collatzRecur(curNum*3+1)

n = int(input())

collatzRecur(n)

#####################################

def collatz(n):
    i = n
    yield i
    while i != 1:
        if i % 2 == 0:
            i //= 2
            yield i
        else:
            i = 3*i + 1
            yield i

print(*list(collatz(int(input()))))

############################################

n=input()
f=lambda n: n!=1 and ([str(n//2)]+ f(n//2) if n%2==0 else [str(n*3+1)] + f(n*3+1)) or []
print(' '.join([n]+f(int(n))))
