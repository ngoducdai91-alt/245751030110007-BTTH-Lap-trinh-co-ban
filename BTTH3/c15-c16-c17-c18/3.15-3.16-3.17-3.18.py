print("NGÔ ĐỨC ĐAI")
print("msv:245751030110007")
print("15)")
day = input("Nhập dãy các từ tiếng Anh (cách nhau bởi dấu cách): ").split()
day.sort() 
print("Các từ sau khi sắp xếp theo thứ tự từ điển:")
for i in day:
    print(i)
print("16)")
chuoi= input("Nhập chuỗi các số nhị phân (cách nhau bởi dấu phẩy, ví dụ: 0100,1010): ")
daynp = chuoi.split(',')
print("Các giá trị nhị phân đã nhập:")
for so in daynp:
    print(so.strip())
print("17)")
def tinh(so):
    tong = 0
    for i in range(1, so // 2 + 1):
        if so % i == 0:
            tong += i
    return tong
n = int(input("Nhập số nguyên dương n: "))
print(f"Các số nguyên dương nhỏ hơn {n} có tổng ước lớn hơn chính nó là:")
for i in range(1, n):
    if tinh(i) > i:
        print(i)
print("18)")
n = int(input("Nhập số nguyên dương n: "))
alist = []
a,b = 0,1
while a < n:
    alist.append(a)
    a,b = b,a + b
print(f"Dãy Fibonacci nhỏ hơn {n}: {alist}")
