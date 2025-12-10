print("NGO DUC DAI")
print("msv 245751030110007")
print("12)")
import re
value=[]
print("Mật khẩu có từ 6-12 kí tự(gồm chữ cái thường, chữ cái in hoa, số, kí tự đặc biệt")
items=[x for x in input("Nhập mật khẩu: ").split(',')]
# ############
for p in items:
   if len(p)<6 or len(p)>12:
      print("Yêu cầu mật khẩu có 6 đến 12 kí tự")
      continue
   else:
      pass
   if not re.search("[a-z]",p):
      print("Không hợp lệ.Yêu cầu mật khẩu có chữ cái thường")
      continue
   elif not re.search("[0-9]",p):
      print("Không hợp lệ.Yêu cầu mật khẩu có ít nhất một số")
      continue
   elif not re.search("[A-Z]",p):
      print("Không hợp lệ.Yêu cầu mật khẩu có chữ cái in hoa")
      continue
   elif not re.search("[$#@]",p):
      print("Không hợp lệ.Yêu cầu mật khẩu có kí tự đặc biệt")
      continue
   else:
      value.append(p)
      print("Mật khẩu hợp lệ")
      print("Mật khẩu của bạn là:")
print(",".join(value))
