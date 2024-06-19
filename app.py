# app.py

# from function import add, multiply # type: ignore

# def main():
#     # Test the add function
#     result_add = add(3, 4)
#     print(f"The sum of 3 and 4 is: {result_add}")

#     # Test the multiply function
#     result_multiply = multiply(3, 4)
#     print(f"The product of 3 and 4 is: {result_multiply}")

# if __name__ == "__main__":
#     main()
# import addition_func.py
from addition_func import add, multiply

num1=int(input("Enter 1st no: "))
num2=int(input("Enter 2nd num: "))
ans=add(num1,num2)
print(ans)