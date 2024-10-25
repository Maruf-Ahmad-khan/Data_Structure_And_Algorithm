class Solution:
     from typing import List
     def Move_zeroes(self, arr : List[int])->None:
          """Don't return anything"""
          
          n = len(arr)
          j = 0
          for i in range(n):
               if arr[i] != 0:
                    arr[i] , arr[j] = arr[j], arr[i]
                    
                    j += 1
               
     def Print_Array(self, arr: List[int])->None:
          for i in arr:
               print(i, end=' ')
               
          print()             
               
if __name__ == "__main__":
     s = Solution()
     arr = [0,1,2,0,3]
     print("Array before moving:")
     s.Print_Array(arr)
     print("Array after moving zeroes:")
     print(s.Move_zeroes(arr))
     s.Print_Array(arr)