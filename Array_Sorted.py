# Check if an Array is Sorted
class Solution:
     from typing  import List

     def Array_Sorted(self, arr : List[int], n : int)->int:
          
          for i in range(n):
               for j in range(i + 1, n):
                    if arr[j] < arr[i]:
                         return False
                    
          return True
     
     
if __name__ == "__main__":
     sol = Solution()
     arr = [1, 2, 3, 4, 5]
     n = len(arr)
     ans = sol.Array_Sorted(arr, n)
     if ans:
          print(True)
          
     else:
          print(False)
     
          