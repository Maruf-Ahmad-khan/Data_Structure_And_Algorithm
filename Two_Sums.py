class Solution :
     from typing import List
     def Two_Sum(self, nums : List[int], target : int)->List[int]:
          num_index = {}
          for i, num in enumerate(nums):
               complement = target - num
               if complement in num_index:
                    return [num_index[complement], i]
               
               num_index[num] = i
               
          return [-1, -1]
     
if __name__ == "__main__":
     sol = Solution()
     nums = [2,7,11,15]
     target = 9
     print('The target is : ')
     print(sol.Two_Sum(nums, target))