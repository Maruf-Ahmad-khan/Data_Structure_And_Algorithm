class Solution:
     #  Max Consecutive Ones
     from typing import List
     def Maxm_Ones(self, nums : List[int])->int:
          
          count = 0
          maxi = 0
          for i in range(len(nums)):
               if nums[i] == 1:
                    count += 1
                    
               else:
                    count = 0
                    
               maxi = max(maxi,  count)

                    
          return maxi
     
     def Print_Array(self, nums : List[int])->None:
          for i in nums:
               print(i, end = " ")
               
          print()
          
if __name__ == "__main__":
     s = Solution()
     nums = [1,1,0,2,1,1,1,1]
     print("Original Array")
     s.Print_Array(nums)
     print("Number of Ones present in the List")
     print(s.Maxm_Ones(nums))
