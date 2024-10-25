class Solution:
     from typing import List
     def D_Rotate(self, num : List[int], k = int)->None:
          
          """"Don't return anything"""
          
          n = len(num)
          # create a new empty list
          ans = [0] *  n
          
          for i in range(n):
               ans [(i+k)%n] = num[i]
          num[:] = ans[:]
          
          
     def Print_Array(self, num : List[int])->None:
          
          for n in num:
               print(n,  end = " ")
               
          print()
          
          
if __name__ == "__main__":
     s = Solution()
     arr = [1,2,3,4,5]
     k = 2
     print("Array before rotation :")
     s.Print_Array(arr)
     
     print("Array after rotation :")
     print(s.D_Rotate(arr, k))
     print(s.Print_Array(arr))



          