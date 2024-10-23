# Optimal Case
class Solution:
     from typing import List
     def Array_Sorted(self, arr : List[int])->bool:
          
          n = len(arr)
          count = 0
          for i in range(1, n):
               if arr[i] < arr[i - 1]:
                    count += 1
                    
          if arr[n - 1] > arr[0]:
               count += 1
          return count <= 1
     
if __name__ == "__main__":
     sol = Solution()
     arr = [1, 2, 3, 4, 5]
     
     if sol.Array_Sorted(arr) == True:
          print("True")
     else:
          print("False")