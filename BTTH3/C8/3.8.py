print("NGÔ ĐỨC ĐAI")
print("msv:245751030110007")
print("8)")
daytu = input("Nhập dãy các từ (cách nhau bởi dấu cách): ").split()
if not daytu:
    print("Dãy từ rỗng.")
else:
    dodaimax = 0
    for tu in daytu:
        if len(tu) > dodaimax:
            dodaimax = len(tu)
    print(f"\nĐộ dài từ dài nhất là: {dodaimax}")
    print("Các từ có độ dài lớn nhất:")
    for tu in daytu:
        if len(tu) == dodaimax:
            print(tu)
