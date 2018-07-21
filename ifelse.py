# 0-40 dc
# 41-60 cb
# 61-80 bb
# 80-100 aa

kul_not = int (input("Notunuzu girin"))

if 0 < kul_not <= 40:
    print("Notunuz dc")
if 40 < kul_not <= 60:
    print("Notunuz cb")
if 60 < kul_not <= 80:
    print("Notunuz bb")
if 80 < kul_not <= 100:
    print("Motunuz aa")

else:
    print ("Tanımsız")