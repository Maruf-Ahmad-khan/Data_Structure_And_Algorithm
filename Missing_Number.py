# Rnage of the number [0, n]

class  Solution:
     from typing import List
     def Missing_Num(self, arr : List[int])->int:
          # calculate the length of the array
          n = len(arr)   
          sum = 0
          # use formula ans = n * (n + 1) / 2
          
          ans =  n * (n + 1) // 2
          
          for i in range(n):
               
               # calculate the sum
               sum = sum + arr[i]
               
          return  ans - sum
     
     
     def Print_Array(self, arr : List[int])->None:
          for i in range(len(arr)):
               print(i , end = ' ')
               
          print()
          
          
if __name__ == "__main__":
     s = Solution()
     arr = [0, 1, 2, 3, 5]
     print("Given List:")
     s.Print_Array(arr)
     
     print("Missing Number is :")
     print(s.Missing_Num(arr))
     # s.Print_Array(arr)


