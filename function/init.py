# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 18:46:50 2018

@author: Ксения
"""
import datetime
#import unittest
"""Сортировка простыми вставками"""

def insertion(data):
	for i in range(len(data)):
		j = i - 1 
		key = data[i]
		while data[j] > key and j >= 0:
			data[j + 1] = data[j]
			j -= 1
		data[j + 1] = key
	return data


timeStart = datetime.datetime.now()
#time.sleep(2)
print(timeStart)    
print(insertion([5,8,1,0,4,9,1,22,33,44,55,6,77,88,99,100,256,478,57,81,31,41,51,61,71,81]))
timeEnd = datetime.datetime.now()
print(timeEnd)
difference = timeEnd - timeStart
print(difference)

def test1():
    return 1

"""Быстрая сортировка"""
import random
def quick_sort(nums):

   if len(nums) <= 1:
       return nums
   else:
       elem = random.choice(nums)
   one_nums = [n for n in nums if n < elem] 

   two_nums = [elem] * nums.count(elem)
   three_nums = [n for n in nums if n > elem]
   
   return quick_sort(one_nums) + two_nums + quick_sort(three_nums)

timeStart = datetime.datetime.now()
print(timeStart)
print(quick_sort([5,8,1,0,4,9,1,22,33,44,55,6,77,88,99,100,256,478,57,81,31,41,51,61,71,81]))
timeEnd = datetime.datetime.now()
print(timeEnd)
difference = timeEnd - timeStart
print(difference)

"""Плавная сортировка"""
def Smooth_Sort(lst):
    def downHeap(lst, k, n):
        new_elem = lst[k]
        while 2*k+1 < n:
            child = 2*k+1
            if child+1 < n and lst[child] < lst[child+1]:
                child += 1
            if new_elem >= lst[child]:
                break
            lst[k] = lst[child]
            k = child
        lst[k] = new_elem
    size = len(lst)
    for i in range(size//2-1,-1,-1):
        downHeap(lst, i, size)
    for i in range(size-1,0,-1):
        temp = lst[i]
        lst[i] = lst[0]
        lst[0] = temp
        downHeap(lst, 0, i)
    return lst

timeStart = datetime.datetime.now()
print(timeStart)
print(Smooth_Sort([5,8,1,0,4,9,1,22,33,44,55,6,77,88,99,100,256,478,57,81,31,41,51,61,71,81]))
timeEnd = datetime.datetime.now()
print(timeEnd)
difference = timeEnd - timeStart
print(difference)

#if __name__ == '__main__':
#    unittest.main()