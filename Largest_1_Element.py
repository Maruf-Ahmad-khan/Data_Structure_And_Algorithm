# Recursive approach
from typing import List
def Largest_Element(arr , n ):
     maxi = arr[0]
     for i in range(0, n):
          if maxi < arr[i]:
               maxi = arr[i]
     return maxi

if __name__ == "__main__":
     arr = [2, 5, 1, 3, 0]
     print("Largest Element is :",  Largest_Element(arr , len(arr)))

     