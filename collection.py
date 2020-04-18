def small(a):
    res = ''
    for i in range(len(a)):
        if ord('A') <= ord(a[i]) <= ord('Z'):
            res += chr(ord(a[i])+32)
        else:
            res+=a[i]
    return res

menuDic = {}
while True:
    menu = input('Enter Menu : ')
    menu = small(menu)
    if menu == 'exit':
        break
    else:
        price = input('Enter Price : ')
        menuDic[menu] = price

summ = 0
print('---------My-Food----------')
for i in menuDic.keys():
    print(i,menuDic[i])
    summ+=int(menuDic[i])
print('Total : %d'%(summ))
print('---------ThankYou---------')