m2000 = m500 = m200 = m100 = m50 = m20 = m10 = m5 = m2 = m1 = 0

money = int(input("enter money to get change: "))



if(money >= 2000):
    m2000 = money // 2000
    money = money % 2000
if(money >= 500):
    m500 = money // 500
    money = money % 500




print("------------------")
print("Amount Change")
print("------------------")
print("RS 2000 -", m2000)
print("RS 500  -", m500)
print("RS 200  -", m200)
print("RS 100  -", m100)
print("RS 50   -", m50)
print("RS 20   -", m20)
print("RS 10   -", m10)
print("RS 5    -", m5)
print("RS 2    -", m2)
print("RS 1    -", m1)
print("------------------")
