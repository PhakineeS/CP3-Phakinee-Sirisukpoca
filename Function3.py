def login():
    id = input("Enter ID : ")
    pw = input("Enter password : ")
    if id == '1' and pw == '2':
        return True
    else:
        return False
def showMenu():
    print('------Shop------')
    print('1.Vat Calculater')
    print('2.Price Calculater')
def menuSelect():
    sel = input('Please Select : ')
    return sel
def vatCal(n):
    return n+(n*0.07)
def priceCal():
    n1 = int(input("First product : "))
    n2 = int(input("Second Product : "))
    return vatCal(n1+n2)

if login():
    showMenu()
    sel = menuSelect()
    if sel == '1':
        n = int(input("Enter Price : "))
        print(vatCal(n))
    else:
        print(priceCal())
else:
    print('Error.Please try again.')