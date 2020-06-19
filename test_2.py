from array import *
A = array('i',[])
n = int(input('Enter number:'))
def solution(A):
    for i in range(n):
        x = int(input('Enter value:'))
        A.append(x)
        print('A[',i,']',A[i])
    A= A[i]*A[i]*A[i]
    print(A)
    return A
solution(A)

