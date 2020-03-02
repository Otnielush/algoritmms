from random import randint
import timeit


def merge_sort(A, s, e):
    global counter
    if s >= e:
        return
    q = (s+e)//2
    merge_sort(A,s,q)
    merge_sort(A,q+1,e)
    merge(A,s,q,e)
    counter += 1
    # print(A[s:e+1])


def merge(A, s, q, e):
    # print("{%d %d %d}" % (round(s,2), round(q, 2), round(e, 2)))
    n = [q-s+1, e-q]
    B = A[s:q+1].copy()
    C = A[q+1:e+1].copy()
    # print(B,C,"= ", end='')
    B.append(0xffffffff)
    C.append(0xffffffff)
    i,j = 0,0
    for k in range(s,e+1):
        if B[i] <= C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j+=1

counter = 0

mass = [12,9,3,7,14,11,6,2,10,5,15,98,4,6,987,6,65,5,1,5,5,3,3,4,5,65,45,95,26,6,49,1,13,9,4]
start = timeit.default_timer()
mass2 = [randint(0,100000000) for x in range(200001)]

stop = timeit.default_timer()
print('Time1: ', stop - start)
start = timeit.default_timer()

merge_sort(mass2,0,len(mass2)-1)
print("\n",len(mass2))
stop = timeit.default_timer()
print('Time2: ', stop - start, 'Counter:', counter)