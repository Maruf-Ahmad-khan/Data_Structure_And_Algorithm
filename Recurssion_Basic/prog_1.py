
def func_1(a: int, b: int)->int:
          
     if a > b:
          return 0
          
     return b + func_1(a, b - 1)

def func_2(a: int , b: int)->int:
     
     if a > b:
          return 0
     
     return a + func_2(a + 1, b)

def func_3(a: int, b: int)->int:
     
     if a > b:
          return 1000
     return a + func_3(a + 1, b)


def main():
     
     result_1 = func_1(3, 8)
     result_2 = func_2(3, 8)
     result_3 = func_3(3, 8)
     print(result_1, result_2, result_3)

if __name__ == "__main__":
     main()     