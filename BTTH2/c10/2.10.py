print("NGÔ ĐỨC ĐẠI")
print("msv:245751030110007")
print("10)")
import math
def Tinh(R):
  if R is None or not isinstance(R, (int, float)) or R < 0:
    print("Lỗi: Bán kính không hợp lệ. Vui lòng nhập một số dương.")
    return None
  else:
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R**2
    return chu_vi, dien_tich
try:
  ban_kinh_input = float(input("Nhập bán kính hình tròn: "))
  ket_qua = Tinh(ban_kinh_input)
  if ket_qua:
    chu_vi, dien_tich = ket_qua
    print(f"Chu vi hình tròn là: {chu_vi:.2f}")
    print(f"Diện tích hình tròn là: {dien_tich:.2f}")
except ValueError:
  print("Lỗi: Đầu vào không phải là một số hợp lệ.")
