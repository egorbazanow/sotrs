import random
import lbsort
import time
N = int(input())
Massiv = [random.randint(1,100000) for i in range(N)]
low = int(min(Massiv))
high = len(Massiv)-1

Start = time.time()
lbsort.bubble_sort(Massiv)
Finish = time.time()
Res_msec = (Finish - Start)*1000
print(Res_msec)

N = int(input())
Massiv = [random.randint(1,100000) for i in range(N)]
Start = time.time()
lbsort.selection_sort(Massiv)
Finish = time.time()
Res_msec = (Finish - Start)*1000
print(Res_msec)

N = int(input())
Massiv = [random.randint(1,100000) for i in range(N)]
Start = time.time()
lbsort.insertion_sort(Massiv)
Finish = time.time()
Res_msec = (Finish - Start)*1000
print(Res_msec)

N = int(input())
Massiv = [random.randint(1,100000) for i in range(N)]
Start = time.time()
lbsort.quick_sort(Massiv, low, high)
Finish = time.time()
Res_msec = (Finish - Start)*1000
print(Res_msec)