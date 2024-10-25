class Solution:
     
     from typing import List
     def Linear_Search(self, arr : List[int], key : int)->int:
          
          n = len(arr)
          for i in range(n):
               if arr[i] == key:
                    return True
               
          return False
     
     def Print(self,  arr : List[int]):
          
          for i in arr:
               print(i, end = ' ')
               
          print()
          
if __name__ == "__main__":
     s = Solution()
     arr = [1,2,3,4,5]
     key = 5
     
     print("Original Array")
     s.Print(arr)
     
     if s.Linear_Search(arr, key) == True:
          print("True")
     else:
          print("False")
