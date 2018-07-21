sozluk = {'one':'bir', 'two':[2,10,3,1]}

#print(sozluk.get('two'))

sozluk['one'] = 1

print(sozluk)

sozluk.update({'two':2})
sozluk.update({'three':3})
print(sozluk)

sozluk['four'] = 4

print(sozluk.items())