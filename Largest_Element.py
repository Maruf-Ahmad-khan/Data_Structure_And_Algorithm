# By Brute Force
class  Solution:

     from typing import List
     def Largest_Element(self, arr : List[int])->int:
          arr.sort()
          return arr[-1]
     
if __name__ == "__main__":
     s = Solution()
     arr = [2, 5, 1, 3, 0]
     print("Largest Element is  : ",  s.Largest_Element(arr))  

