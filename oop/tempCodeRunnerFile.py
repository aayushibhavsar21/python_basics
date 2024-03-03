
import numpy as np

class Solution(object):
    def findMedianSortedArrays(arr):
        arr = np.sort(arr)
        if len(arr)%2 != 0 :
            print ( arr[int(len(arr)/2)])
        else :
            print ( (arr[int(len(arr)/2)-1] + arr[int(len(arr)/2)])/2)
       
arr1 = np.array([1, 2 ])
arr2 = np.array([3 , 4])

arr = np.concatenate((arr1, arr2))
print(arr)

s = Solution
s.findMedianSortedArrays(arr)