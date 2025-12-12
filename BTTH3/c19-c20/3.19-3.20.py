print("NGÔ ĐỨC ĐAI")
print("msv:245751030110007")
print("19)")
def sieve_of_eratosthenes(limit):
    is_p = [True] * (limit + 1)
    if limit >= 0:
        is_p[0] = False
    if limit >= 1:
        is_p[1] = False
    for p in range(2, int(limit**0.5) + 1):
        if is_p[p]:
            for i in range(p*p, limit + 1, p):
                is_p[i] = False
    prime_numbers = [p for p, is_p_val in enumerate(is_p) if is_p_val]
    return tuple(prime_numbers)
limit = 1000000
P = sieve_of_eratosthenes(limit)
print(f"Kiểu dữ liệu của P là: {type(P)}")
print(f"Tổng số nguyên tố tìm được: {len(P)}")
print(f"10 số nguyên tố đầu tiên: {P[:10]}")
print(f"5 số nguyên tố cuối cùng: {P[-5:]}")
print("DO CHƯƠNG TRÌNH DÀI NÊN IN RA 10 SỐ ĐẦU 5 SỐ CUỐI")
print("20)")
import math
def pascal_triangle(n_rows):
      for i in range(n_rows):
        row_values = []
        for j in range(i + 1):
            coeff = 1
            if j > i - j:
                j = i - j
            for k in range(j):
                coeff = coeff * (i - k) // (k + 1)
            row_values.append(str(coeff))     
        print(" ".join(row_values))
try:
    n_input = int(input("Nhập số dòng n: "))
    if n_input <= 0:
        print("Vui lòng nhập một số nguyên dương.")
    else:
        print(f"--- Tam giác Pascal với {n_input} dòng ---")
        pascal_triangle(n_input)
except ValueError:
    print("Đầu vào không hợp lệ. Vui lòng nhập một số nguyên.")
