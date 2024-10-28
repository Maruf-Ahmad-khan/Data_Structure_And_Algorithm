class Solution:
     from typing import  List

     def Two_Sum(self, nums: List[int],  target: int) -> List[int]:
          n = len(nums)
          for i in range(n):
               for j in range(i + 1, n):
                    if nums[i] + nums[j] == target:
                         return [i, j]
                    
          return []
     
if __name__ == "__main__":
     sol = Solution()
     nums = [2,7,11,15]
     target = 9
     print('The target is : ')
     print(sol.Two_Sum(nums, target))
     
          
