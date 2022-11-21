#!/usr/bin/env python
# coding: utf-8

# In[4]:


'''
1. Створіть функцію, яка обчислює факторіал числа. Запустіть декілька
задач, що використовуватимуть ТРгеадРооіЕхесцог. Виміряти швидкість
обчислень. Зробіть теж саме, використовуючи Ргосез5РооіЕхесиог.
Додайте у програму код, який порівнює швидкість обчислень і виводить на
друк найоптимальніший метод.
'''

from concurrent.futures import ProcessPoolExecutor
from concurrent.futures import ThreadPoolExecutor
from math import factorial
import time

times_check = []

def factor(numb):
    started_at = time.time()
    fact = factorial(numb)
    print(f'factorial {numb} = {fact}')
    timer = time.time() - started_at
    print(f'Time: {timer}')
    times_check.append(timer)
    
def main():    
    with ProcessPoolExecutor(max_workers=4) as executor:
        task1 = executor.submit(factor(150))
        task2 = executor.submit(factor(250))
        task3 = executor.submit(factor(350))
        task4 = executor.submit(factor(500))

def main2():    
    with ThreadPoolExecutor(max_workers=4) as executor:
        task1 = executor.submit(factor(150))
        task2 = executor.submit(factor(250))
        task3 = executor.submit(factor(350))
        task4 = executor.submit(factor(500))    

main()
main2()

def winner():
    process_pool = sum(times_check[0:3])
    thread_pool = sum(times_check[4:7])
    if process_pool > thread_pool:
        print("ThreadPoolExecutor - WIN")
    if process_pool < thread_pool:
        print("ProcessPoolExecutor - WIN")

winner()        


# In[ ]:




