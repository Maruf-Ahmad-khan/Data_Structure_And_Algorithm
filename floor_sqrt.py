class Solution:
     
     def floorsqrt(self, n):
          
          low = 1
          high = n
          while low <= high:
               mid = low + (high - low) // 2
               value = mid * mid 
               if value <= n:
                    low = mid + 1
               else:
                    high = mid - 1
                    
          return high
     
     
sol = Solution()
n = 17
print("The square root is : ")
print(sol.floorsqrt(n))