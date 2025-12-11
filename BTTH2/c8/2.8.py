print("NGÔ ĐỨC ĐẠI")
print("msv:245751030110007")
print("8)")
import math
pos = [0, 0]
print("Nhập các lệnh di chuyển theo quy định. Nhấn Enter 2 lần để kết thúc.")
while True:
    try:
        s = input()
        if not s:
            break
        movement = s.split(" ")
        direction = movement[0].upper()
        steps = int(movement[1])
        if direction == "UP":
            pos[0] += steps
        elif direction == "DOWN":
            pos[0] -= steps
        elif direction == "LEFT":
            pos[1] -= steps
        elif direction == "RIGHT":
            pos[1] += steps
        else:
            print(f"Lệnh không hợp lệ: {s}")
            pass  
    except EOFError:
        break
    except ValueError:
        print(f"Lỗi: Số bước không hợp lệ trong lệnh: {s}")
distance = math.sqrt(pos[1]**2 + pos[0]**2)
print(f"\nKhoảng cách cuối cùng đến điểm (0,0) là: {distance:.2f}")
print(f"Kết quả (làm tròn số nguyên gần nhất): {int(round(distance))}")
