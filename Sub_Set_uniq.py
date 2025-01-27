class Solution:
     
     from typing import List
     
     def generate_All_Subsets(self, nums : List[int], curr : int,  ds : List[int], ans : set):
          
          if curr == len(nums):
               ans.add(tuple(ds))
               return
          currval = nums[curr]
          ds.append(currval)
          self.generate_All_Subsets(nums, curr + 1, ds, ans)
          ds.pop()
          self.generate_All_Subsets(nums, curr + 1, ds, ans)
     
     def  subsetsWithDup(self, nums: List[int])->List[List[int]]:
          
          ans = set()
          ds = []
          nums.sort()
          self.generate_All_Subsets(nums, 0, ans, ds)
          return [list(subset) for subset in ans]
          