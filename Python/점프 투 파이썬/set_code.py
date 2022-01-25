"""
a = set('abcdefgh') # {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'}
b = set('cdef') # {'c', 'd', 'e', 'f'}
c = set('efgh') # {'e', 'f', 'g', 'h'}

print("a: ", a)
print("b: ", b)
print("c: ", c)

print("a | b : ", a | b) 
print("a - c : ", a - c)
print("a & b & c : ", a & b & c)

a = input()
print(set(a.split()))

"""

"""
a = { 'a' : 'b', 'b' : 'e' }
print("a : ", a)
a['a'] = 'c'
print("a : ", a)
print(a.keys())
print(a.values())
print(a.items())

for i in a.keys():
    print(i, ':', a[i])
"""

a = { 'name' : 'john', 'phone' : '01012345678', 
    'email' : 'test@test.com', 'birth' : 1111 }
print("name :", a['name']) # john

a['birth'] = 1010
print("birth :", a['birth']) # 1010

a['city'] = 'seoul'
print("a :", a);
