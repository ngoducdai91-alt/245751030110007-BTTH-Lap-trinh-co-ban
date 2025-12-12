print("NGÔ ĐỨC ĐAI")
print("msv:245751030110007")
print("9)")
ds=input("Nhập chuỗi:").split()
print("10)")
print("Chuỗi bài 9 sau khi bỏ phần đầu và cuối:")
x=ds[1:-1]
for c in x:
    print(c)
print("11)")
print("Chuỗi bài 9 sau khi thêm abc và 123 cuối chuỗi:")
ds.append("abc")
ds.append("123")
for ch in ds:
    print(ch)
print("12)")
print("Chuỗi bài 9 sau khi bỏ 123:")
ds.remove("123")
for ch in ds:
    print(ch)
print("13)")
print("vị trí của chuỗi abc trong chuỗi bài 9 là:",ds.index("abc"))
print("14)")
print("Chuỗi bài 9 sau khi sắp xếp")
ds.sort()
for ch in ds:
    print(ch)
