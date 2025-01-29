# Problem statement
# Given two sorted arrays 'a' and 'b' of size 'n' and 'm' respectively.
# Find the median of the two sorted arrays.
# Median is defined as the middle value of a sorted list
# of numbers. In case the length of list is even, median 
# is the average of the two middle elements.
# Brute Force Solution

# I will use third array to store the sorted element arr3 size would be (n1 + n2)

class Solution:
     from typing import List
     def Medians(self, a:List[int], b:List[int])->float:
          n1 = len(a)
          n2 = len(b)
          i = 0
          j = 0
          arr = []
          
          while i < n1 and j < n2:
               if a[i] < b[j]:
                    arr.append(a[i])
                    i += 1
                    
               else:
                    arr.append(b[j])
                    j += 1
                    
                    
          arr.extend(a[i:])
          arr.extend(b[j:])
          
          n = n1 + n2
          if n % 2 == 1:
               return float(arr[n // 2])
          
          median = (arr[n // 2] + arr[(n // 2) - 1]) / 2.0
          return median
     
ans = Solution()
a = [1,3]
b =  [2]
print("The median is :", ans.Medians(a, b)  )
            