tupla = (1, 2, 3, 4, 5)

uno, dos, *_, cinco = (tupla)

print(uno)
print(dos)
print(*_) #resto de valores (3,4) 
print(cinco)


lista = [1, 2, 3, 4, 5]
sub_lista = lista[-3:]
print(sub_lista)


print(False or False or True) #True
print('false' or () or []) #false
print((1) or False or []) #1
print(() or {} or []) #[]

d1 = {'a':1, 2:10}
d2 = {10:1, 2:10}
d3 = {True: True, False: False}
#d4 = {{12}:12, (13,2):True}  TyError: type 'set' (no es dict)
print(d1)
print(d2)
print(d3)
print(d4)