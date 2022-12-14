import time

#Non recursive
def iterative_fib(n): #Time complexity O(n)
    a, b = 0, 1
    for i in range(n):
        a, b = b, (a+b)
    return a

def sum_fib(n): #Time complexity O(n^2), inefficient
    counter = 0
    for i in range(n):
        counter += iterative_fib(i)
    return counter
st = time.time()
sum_fib(1000)
et = time.time()
elapsed_time = (et - st) * 1000
print(f"sum_fib exectution time: {elapsed_time} milliseconds for n = 1000")

st = time.time()
sum_fib(10000)
et = time.time()
elapsed_time = (et - st) * 1000
print(f"sum_fib exectution time: {elapsed_time} milliseconds for n = 10000")

def better_sum_fib(n): #Time complexity O(n)
    if n < 2:
        return n
    lst_fib = [0, 1]
    sum_better = [0, 1]
    for i in range(n):
        lst_fib.append(lst_fib[-1] + lst_fib[-2])
        sum_better.append(lst_fib[-1] + sum_better[-1])
    return sum_better[-1]

st = time.time()
better_sum_fib(1000)
et = time.time()
elapsed_time = (et - st) * 1000
print(f"better sum_fib exectution time: {elapsed_time} milliseconds for n = 1000")


st = time.time()
better_sum_fib(10000)
et = time.time()
elapsed_time = (et - st) * 1000
print(f"better sum_fib exectution time: {elapsed_time} milliseconds for n = 10000")

#Useful sums
def tri_num(n): #Time complexity O(n^2), essentially sum_fib
    counter = 0
    for i in range(n):
        for j in range(i):
            #Do something O(1) time
            counter += 1
    return counter

#def func(n): #Time complexity O(n^(k + 1))
#    counter = 0
#    for i in range(n):
#        #Do something O(i^k) time (Number of loops in the inner loop)
#    return counter


#Recursive (Exponentiation)
#Time taken to get base^pow given base and pow

def my_pow(base, power): #Inefficient, O(n)
    if power == 0:
        return 1
    else:
        return base * my_pow(base, power - 1)

def better_my_pow(base, power): #More efficient, O(logn)
    if power == 0:
        return 1
    half_pow = better_my_pow(base, power//2)
    if power % 2 == 0:
        return half_pow * half_pow
    return base * half_pow * half_pow

def worse_my_pow(base, power): #What if my_pow(base, power//2) calculated twice? O(n)
    if power == 0:
        return 1
    if power % 2 == 0:
        return worse_my_pow(base, power//2) * worse_my_pow(base, power//2)
    return base * worse_my_pow(base, power//2) * worse_my_pow(base, power//2)
