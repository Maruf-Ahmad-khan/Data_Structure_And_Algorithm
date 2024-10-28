class Solution:
     def Power_of_two(self, n: int)->bool:
          if n == 1:
               return True
          
          if n == 0 or n % 2 != 0:
               return False
          return self.Power_of_two(n / 2)
     
sol = Solution()
n = 16
print(sol.Power_of_two(n))