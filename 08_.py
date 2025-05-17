# class student:
#     def __init__(self, physics, chemistry, maths):
#         self.phy = physics
#         self.chem = chemistry
#         self.math = maths
#         self.percentage = str((self.phy + self.chem + self.math) / 3) + "%"
# stu1= student(90, 80, 70)
# print(stu1.percentage)
# stu2= student(60, 70, 80)
# print(stu2.percentage)  
# stu3= student(50, 60, 70)
# print(stu3.percentage)
# stu4= student(40, 50, 60)
# print(stu4.percentage)


# complex number project
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
        def showNumber(self):
            print(self.real, "i", self.imag, "i")
num1 = Complex(2, 3)
num1.showNumber()
num2 = Complex(4, 5)
num2.showNumber()
