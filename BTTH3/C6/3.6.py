print("NGÔ ĐỨC ĐAI")
print("msv:245751030110007")
print("6)")
x= input("Nhập họ và tên đầy đủ (ví dụ: Nguyen Van A): ")
y = x.split()
if len(y) >= 2:
    ho = y[0]
    ten = y[-1]
    print("\n--- Kết Quả ---")
    print(f"Họ: {ho}")
    print(f"Tên riêng: {ten}")
else:
    print("Vui lòng nhập họ và tên hợp lệ (có ít nhất 2 từ).")
