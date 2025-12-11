print("NGÔ ĐỨC ĐẠI")
print("msv:245751030110007")
print("11)")
def benefit(t, n, k):
    interest_rate = t / 100
    total_money = n * (1 + interest_rate)**k
    return total_money
t = float(input("Nhập lăi xuất:"))
n = float(input("Nhập số tiền gửi ban đầu:"))
k = int(input("Nhập số tháng gửi:"))
total = benefit(t, n, k)
print(f"Số tiền nhận được sau {k} tháng là: {total:.2f} VNĐ")

