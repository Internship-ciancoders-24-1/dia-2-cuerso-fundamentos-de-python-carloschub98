rae = {}
rae['pizza'] = 'Delicioso'

print(rae)

#validando si existe la key o no
a = rae.get('helado', None)
print(a)

a = rae.get('pizza', None)
print(a)

print(rae.keys())

print(rae.values())

print(rae.items())

