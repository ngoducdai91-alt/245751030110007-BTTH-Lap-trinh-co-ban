print("NGÔ ĐỨC ĐAI")
print("msv:245751030110007")
print("7)")
chuoigoc = input("Nhập một chuỗi (bao gồm chữ và số): ")
chuoimoi = ""
for kitu in chuoigoc:
    if not kitu.isdigit():
        chuoimoi += kitu
print(f"Chuỗi mới sau khi loại bỏ chữ số: {chuoimoi}")
