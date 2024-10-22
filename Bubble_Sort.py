class Solution:
     from typing import List
     def Bubble_Sort(self, arr : List[int])->None:
          n = len(arr)
          for i in range(n - 1):
               flage = 0
               for j in range(n - i - 1):
                    if (arr[j] > arr[j + 1]):
                         arr[j], arr[j + 1] = arr[j + 1], arr[j]
                         flage = 1
               if flage == 0:
                    break
               
               
     def Print_Array(self, arr : List[int])->None:
          for i in arr:
               print(i, end = " ")
               
          print()
          

if __name__ == "__main__":
     sol = Solution()
     arr = [9, 8, 7, 1, 3, 2, 4]
     
     print("Array before sorting")
     sol.Print_Array(arr)
     
     print("Array after sorting")
     sol.Bubble_Sort(arr)
     sol.Print_Array(arr)