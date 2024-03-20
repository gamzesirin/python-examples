tuple1=(1,3,5,7)
for sayi in tuple1:
    print(sayi)


liste = [[1,2,3],[4,5,6],["a","b","c"]]
for x,y,z in liste:
    print(x,y,z)

liste = [[1,2],[4,5],[3,9]]
for x,y in liste:
    print(x*y)


kullanici1={
    "ad":"gamze",
    "soyad":"şirin"
}
print(kullanici1)
print(kullanici1.values())
print(kullanici1.keys())
print(kullanici1.items())

for k,v in kullanici1.items():
    print("key: {} \t value: {}".format(k,v))

for k in kullanici1.keys():
    print("key: {}".format(k))