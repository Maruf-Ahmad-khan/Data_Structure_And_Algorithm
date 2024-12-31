def func(a:int)->int:
     
     if a == 10:
          return a
     return a + func(a + 1)

def func1(a:int)->int:
     
     try:
          if a == 0:
               return a
          return a + func1(a+1)
     except Exception as e:
          print(f"Error: {e}")


def main():
     res = func(6)
     res1 = func1(6)
     print(res)
     print(res1)
     
if __name__ == "__main__":
     main()