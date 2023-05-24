import BMI
import test10

cone = test10.Cone()

cone1 = test10.PCone()

print(cone.get_vol())

person1 = BMI.BMI("lee", 35, 90, 182)

print(person1.name+"님")
print("나이 : " ,person1.age)
print("몸무게 : " ,person1.weight)
print("키 : " ,person1.height)
print("비만도 : ", person1.get_status())

