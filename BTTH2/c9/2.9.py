print("NGÔ ĐỨC ĐẠI")
print("msv:245751030110007")
print("9)")
def add(x, y):
 return x + y
def subtract(x, y):
 return x - y
def multiply(x, y):
 return x * y
def divide(x, y):
 return x / y
print("Select operation.")
print("1.CỘNG")
print("2.TRỪ")
print("3.NHÂN")
print("4.CHIA")
choice = input("Chọn phép tính(1̣/2/3/4):")
num1 = int(input("Nhập hạng số thứ nhất: "))
num2 = int(input("Nhập hạng số thứ hai: "))
if choice == '1':
 print(num1,"+",num2,"=", add(num1,num2))
elif choice == '2':
 print(num1,"-",num2,"=", subtract(num1,num2))
elif choice == '3':
 print(num1,"*",num2,"=", multiply(num1,num2))
elif choice == '4':
 print(num1,"/",num2,"=", divide(num1,num2))
else:
 print("Invalid input")
