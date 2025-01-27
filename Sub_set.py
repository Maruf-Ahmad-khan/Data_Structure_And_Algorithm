class Solution:
     
     def generateAllSubset(self, nums, CurrIndex, res, powerset):
          
          if CurrIndex >= len(nums):
               powerset.append(res[:])
               return 
          
          CurrVal = nums[CurrIndex]
          res.append(CurrVal)
          self.generateAllSubset(nums, CurrIndex + 1, res, powerset)
          
          res.pop()
          self.generateAllSubset(nums, CurrIndex + 1, res, powerset)
     
     
     
     def Subset(self, nums):
          
          res = []
          powerset = []
          self.generateAllSubset(nums, 0,  res, powerset)
          return powerset
     
     
     