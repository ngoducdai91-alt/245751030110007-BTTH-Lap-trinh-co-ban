print("NGÔ ĐỨC ĐAI")
print("msv:245751030110007")
print("################################")
print("24)")
print("Vui lòng nhập một câu:")
input_string = input()
upper_count = 0
lower_count = 0
for char in input_string:
    if char.isupper():
        upper_count += 1
    elif char.islower():
        lower_count += 1
print(f"Chữ hoa: {upper_count}")
print(f"Chữ thường: {lower_count}")
print("25)")
def filter():
    input_str = input("Nhập các số (phân tách bằng dấu phẩy, ví dụ: 1,2,3,4,5,6,7,8,9): ")
    numbers_list = []
    for item in input_str.split(','):
        try:
            numbers_list.append(int(item.strip()))
        except ValueError:
            continue
    odd_numbers = [num for num in numbers_list if num % 2 != 0]
    output_str = ",".join(map(str, odd_numbers))
    print(f"Đầu ra (các số lẻ đã lọc): {output_str}")
if __name__ == "__main__":
    filter()
print("26)")
def calculate():
    balance = 0
    print("Nhập nhật ký giao dịch (Ví dụ: D 100 hoặc W 50).")
    print("Nhấn Enter liên tiếp 2 lần (dòng trống) để kết thúc nhập liệu.")
    while True:
        transaction = input()
        if not transaction:
            break 
        parts = transaction.split()
        if len(parts) != 2:
            print(f"Cảnh báo: Định dạng không hợp lệ cho dòng '{transaction}'. Vui lòng nhập đúng 'D [số tiền]' hoặc 'W [số tiền]'.")
            continue 
        trans_type = parts[0].upper()         
        try:
            amount = int(parts[1])
        except ValueError:
            print(f"Cảnh báo: Số tiền không hợp lệ cho dòng '{transaction}'. Vui lòng nhập số nguyên.")
            continue
        if trans_type == 'D':
            balance += amount
        elif trans_type == 'W':
            balance -= amount
        else:
            print(f"Cảnh báo: Loại giao dịch không xác định '{trans_type}'. Chỉ chấp nhận 'D' hoặc 'W'.")
            continue
    print(f"Đầu ra (Số tiền thực trong tài khoản): {balance}")
if __name__ == "__main__":
    calculate()



