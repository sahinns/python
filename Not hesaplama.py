# 0-40 dc
# 41-60 cb
# 61-80 bb
# 80-100 aa

vize = int(input ("Vize Notunuzu girin"))
final= int(input ("Final Notunuzu girin"))

sonuc = int((vize*0.4) + (final*0.6))

if 0 < sonuc <= 40:
    print("Notunuz dc")
elif 40 < sonuc <= 60:
    print("Notunuz cb")
elif 60 < sonuc <= 80:
    print("Notunuz bb")
elif 80 < sonuc <= 100:
    print("Notunuz aa")

else:
    print ("Tanımsız")