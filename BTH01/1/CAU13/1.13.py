print("NGO DUC DAI")
print("msv 245751030110007")
print("13)")
# giai phuong trinh bac 2
import math
a=int(input( "nhap gia tri a"))
b=int(input("nhap gia tri b"))
c=int(input("nhap gia tri c"))
d=b*b-4*a*c
if d<0:
    print("phuong trinh vo nghiem")
elif d>0:
    x1=(-b-math.sqrt(d))/(2*a)
    x2=(-b+math.sqrt(d))/(2*a)
    print("phuong trinh co 2 nghiem phan biet",x1,x2)
elif d==0:
    x=-b/2*a
    print("phuong trinh co nghiem kep",x)

