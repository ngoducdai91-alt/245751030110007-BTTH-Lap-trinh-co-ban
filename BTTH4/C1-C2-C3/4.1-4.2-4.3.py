print("NGÔ ĐỨC ĐAI")
print("msv:245751030110007")
print("################################")
print("1)")
class Circle(object):
    def __init__(self, r):
        self.radius = r
    def area(self):
        return self.radius**2 * 3.14

aCricle = Circle(5)
print(aCricle.area())
print("2)")
class Hinhchunhat(object):
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong
    def area(self):
        return self.dai * self.rong
    
hinh_chu_nhat = Hinhchunhat(8,10)
print(hinh_chu_nhat.area())
hinh_chu_nhat = Hinhchunhat(5,10)
print(hinh_chu_nhat.area())
print("3)")
class Nguoi(object):
    def getGender(self):
        return "Unknown"
class Nam(Nguoi):
    def getGender(self):
        return "Nam"
class Nu(Nguoi):
    def getGender(self):
        return "Nữ"
    
aNam = Nam()
aNu = Nu()
print(aNam.getGender())
print(aNu.getGender())
