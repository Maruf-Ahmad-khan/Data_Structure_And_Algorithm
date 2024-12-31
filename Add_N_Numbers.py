# write a recurssive function to add n numbers:

def Add_n_numbers(n: int)->int:
     
     if n == 0:
          return 0
     num = int(input('Enter a number: \n'))
     return num + Add_n_numbers(n - 1)


n = int(input("How many numbers do you want to add ?"))
result = Add_n_numbers(n)
print("The result is :\n", result)