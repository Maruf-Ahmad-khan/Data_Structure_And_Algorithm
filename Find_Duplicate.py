# optimal Solution
class Solution:
     from typing import  List
     def Duplicate(self, arr : List[int])->int:
          
          i = 0
          for j in range(1, len(arr)):
               if arr[i] != arr[j]:
                    i += 1
                    arr[i] = arr[j]
                    
          return i + 1
     
     
     def Print_Array(self, arr : List[int])->None:
          for i in arr:
               print(i, end = " ")
          print()
     
if __name__ == "__main__":
     sol = Solution()
     arr = [1,1,2,2,3,3]
     print("Original Array")
     sol.Print_Array(arr)
     
     print("Array without Duplicate")
     sol.Duplicate(arr)
     sol.Print_Array(arr)
          